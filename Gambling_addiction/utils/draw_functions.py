import pygame
import const
from tkinter import *
from tkinter import messagebox
import utils.file_utils as file_utils
import text_messages
import utils.utils as utils
import classes.items_class as item_class

def draw_message_box(title, text):
    messagebox.showinfo(title, text)

def draw_centered_text_with_other_element_as_reference_point(screen, text, font, colour, reference_rect, x_offset):
    surface = font.render(text, True, colour)
    rect = surface.get_rect()
    rect.midleft = (reference_rect.right + x_offset, reference_rect.centery)
    screen.blit(surface, rect)

def draw_text(surface, text, color, rect, font, line_spacing=0, antialias=True):
    x, y = rect.topleft
    max_width = rect.width

    # Split the text on words
    words = text.split(' ')
    line = ""
    
    for word in words:
        # Temporarly adding word to the current line
        test_line = line + word + " "
        # Measuring line width
        line_width, _ = font.size(test_line)
        
        #If the line is wider than max width, we draw current line
        if line_width > max_width:
            rendered_line = font.render(line, antialias, color)
            surface.blit(rendered_line, (x, y))
            y += font.get_linesize() + line_spacing
            line = word + " "  #New line starts with current word
        else:
            line = test_line

    # Draw the rest of the text
    if line:
        rendered_line = font.render(line, antialias, color)
        surface.blit(rendered_line, (x, y))

def draw_button(surface, colour, rect, text, font, text_color, mouse_pos = (0, 0)):
    hover_red = 0
    hover_green = 0
    hover_blue = 55
    hover_colour =() #colour
    if rect.collidepoint(mouse_pos):
        hover_colour = determine_colour(hover_red, hover_green, hover_blue, hover_colour, colour)
    else:
        hover_colour = colour
    pygame.draw.rect(surface, hover_colour, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)

def determine_colour(hover_red, hover_green, hover_blue, hover_colour, colour):
    r = colour[0] #taking colour red, which is the first element of the colour tupple
    g = colour[1] #taking colour green, which is the second element of the colour tupple
    b = colour[2] #taking colour blue, which is the third element of the colour tupple
    if r <= 255 and r + hover_red <= 255:
            r = r + hover_red
            hover_colour = hover_colour + (r,)
    else:
        hover_colour = hover_colour + (r,)
    if g <= 255 and g + hover_green <= 255:
            g = g + hover_green
            hover_colour = hover_colour + (g,)
    else:
        hover_colour = hover_colour + (g,)
    if b <= 255 and b + hover_blue <= 255:
            b = b + hover_blue
            hover_colour = hover_colour + (b,)
    else:
        hover_colour = hover_colour + (b,)
    return hover_colour        

def draw_title(screen, color, text = "GAMBLING ADDICTION"):
    font_size = 100
    # Create font object
    title_font = pygame.font.Font(None, font_size)

    title_text = text
    title_surface = title_font.render(title_text, True, color)
    title_rect = title_surface.get_rect(center=((screen.get_width() - 50) // 2, screen.get_height() / 12))
    
    screen.blit(title_surface, title_rect)

def cache_and_get_images_and_icons(imagePath, images_cache, size=None):
    key = (imagePath, size)
    if key not in images_cache:
        loaded_image = pygame.image.load(file_utils.resource_path(imagePath)).convert_alpha()
        if size:
            loaded_image = pygame.transform.scale(loaded_image, size)
        images_cache[key] = loaded_image
    return images_cache[key]

def load_background_image(screen, imagePath):
    size = (const.screen.get_width(), const.screen.get_height())
    image = cache_and_get_images_and_icons(imagePath, const.images_cache, size)
    screen.blit(image, (0, 0))

def load_icons(screen, iconPath, icon_width, icon_height, icon_position_x, icon_position_y):
    size = (icon_width, icon_height)
    icon = cache_and_get_images_and_icons(iconPath, const.images_cache, size)
    screen.blit(icon, (icon_position_x, icon_position_y))
    return icon_position_x, icon_position_y, icon_width, icon_height

def draw_text_box(screen, colour, rect, text, font, text_color):
        txt_surface = font.render(text, True, text_color)
        pygame.draw.rect(screen, colour, rect, 2)
        const.screen.blit(txt_surface, (rect.x + 5, rect.y + 5))

def draw_custom_message_box(screen, text, font):
    box_rect = pygame.Rect(const.screen.get_width()/2-150, const.screen.get_height()/2-25, 300, 50)
    pygame.draw.rect(screen, const.white, box_rect)
    pygame.draw.rect(screen, const.white, box_rect, 3)

    msg_surface = font.render(text, True, const.black)
    msg_rect = msg_surface.get_rect(center=box_rect.center)
    screen.blit(msg_surface, msg_rect)

def draw_info_cards(screen):
    screen_width = const.screen.get_width() #take screen width
    x_coordinate = 100
    y_coordinate = 100
    card_width = 200
    card_height = 200
    title_font_size = 40
    button_font_size = 30
    title_counter = 0
    title_font = pygame.font.SysFont(None, title_font_size, bold = True)
    button_font_size = pygame.font.SysFont(None, button_font_size, bold = False)
    button = []
    for i in const.jobs_list:
        pygame.draw.rect(screen, const.job_box, pygame.Rect(x_coordinate, y_coordinate, card_width, card_height))

        salary_text = "Monthly: " + str(const.jobs_list[title_counter][1])
        title_text = const.jobs_list[title_counter][0]
        description_text = const.jobs_list[title_counter][2]
        title_surface = title_font.render(title_text, True, const.job_cards_text)
        salary_surface = button_font_size.render(salary_text, True, const.job_cards_text)
        title_rect = title_surface.get_rect(center=(x_coordinate + (card_width / 2), y_coordinate + 30))
        salary_rect = salary_surface.get_rect(center=(x_coordinate + (card_width / 2), y_coordinate + 130))

        draw_text(screen, description_text, const.job_cards_text, pygame.Rect(x_coordinate, y_coordinate + 50, card_width, card_height), button_font_size, line_spacing=2)
        draw_button(screen, const.job_button, pygame.Rect(x_coordinate + 20, y_coordinate + 150, 160, 40), "View details", button_font_size, const.job_cards_text)
        button.append(x_coordinate + 20) 
        button.append(y_coordinate + 150) 
        button.append(title_text) 
        button.append(salary_text) 
        button.append(description_text)
        button.append([x_coordinate + 20, y_coordinate + 150, 160, 40])
        const.buttons_list.append(button)
        button = []

        screen.blit(title_surface, title_rect)
        screen.blit(salary_surface, salary_rect)
        x_coordinate += 300
        if x_coordinate + 100 == screen_width:
            y_coordinate += 250
            x_coordinate = 100
        title_counter += 1
 
def draw_card(screen, button_colour = None, button_text_colour = None, num_of_buttons = 0, button_text_list = [], icons = None):
    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()
    rect_list = []
    short = False
    current_text = ""
    card_width = screen_width / 3.5 
    card_height = screen_height / 1.2 
    x_coordinate = screen_width / 2 - card_width / 2
    y_coordinate = screen_height / 1.8 - card_height / 2 
    button_width = card_width / (num_of_buttons + 1)
    button_height = card_height / 12.5
    if not isinstance(icons, item_class.apartment):
        icon_width = card_width - card_width / 10
        icon_height = card_height - card_height / 5
    if isinstance(icons, item_class.apartment):
        icon_width = card_width - card_width / 10
        icon_height = card_height - card_height / 4
    pygame.draw.rect(screen, const.job_box, pygame.Rect(x_coordinate, y_coordinate, card_width, card_height))
    displacement = button_width / (num_of_buttons + 1) 
    button_position_x = x_coordinate + displacement 
    button_position_y = card_height + card_height / 16.666666667
    button_font_size = int(button_width / 2)
    button_font_size = pygame.font.SysFont(None, button_font_size, bold = False)
    if len(button_text_list) < num_of_buttons:
        short = True
    for i in range(num_of_buttons):
        button_rect = pygame.Rect(button_position_x, button_position_y, button_width, button_height)
        rect_list.append(button_rect)
        if short and i < len(button_text_list):
            current_text = button_text_list[i]
            draw_button(screen, button_colour, button_rect, current_text, button_font_size, button_text_colour)
        elif short and i >= len(button_text_list):
            draw_button(screen, button_colour, button_rect, current_text, button_font_size, button_text_colour)
        elif not short:
            draw_button(screen, button_colour, button_rect, button_text_list[i], button_font_size, button_text_colour)
        button_position_x = button_position_x + displacement + button_width
    if icons != None and not isinstance(icons, item_class.apartment):
        load_icons(screen, icons.image_path, icon_width, icon_height, x_coordinate + card_width / 20, y_coordinate + card_height / 25)
    if icons != None and isinstance(icons, item_class.apartment):
        font = pygame.font.SysFont(None, 25)
        load_icons(screen, icons.image_path, icon_width, icon_height, x_coordinate + card_width / 20, y_coordinate + card_height / 25)
        price_text_rect  = pygame.Rect(x_coordinate + card_width / 20, y_coordinate + card_height / 15 + icon_height, card_width / 2, card_height / 5)
        draw_text(screen, f"Buy price: {icons.price}", const.black, price_text_rect, font, line_spacing = 5)
        price_text_rect  = pygame.Rect(x_coordinate + card_width / 30 + card_width / 2, y_coordinate + card_height / 15 + icon_height, card_width / 2, card_height / 5)
        draw_text(screen, f"Rent expenses: {icons.renting_expenses}", const.black, price_text_rect, font, line_spacing = 5)
    return rect_list

def show_fps_counter(screen, clock, text_colour, text_rect, font, clock_value, line_spacing = 5):
    pygame.font.init()
    font = pygame.font.SysFont(None, 30, False, True)
    fps = clock.get_fps()
    draw_text(screen, f"FPS: {round(fps, 2)}", text_colour, text_rect, font, line_spacing)
    clock.tick(clock_value) 

def gather_animated_spin_animations(icon_path, icon_width, icon_height, angle, COUNTER_CLOCK_WISE = True):
    rotated_image = []
    size = (icon_width, icon_height)
    original_icon = cache_and_get_images_and_icons(icon_path, const.wheel_spin_cache, size)
    if COUNTER_CLOCK_WISE:
        for i in range(0, 360, angle):
            rotated_image.append(pygame.transform.rotate(original_icon, i))
        return rotated_image
    elif not COUNTER_CLOCK_WISE:
        for i in range(360, 0, -angle):
            rotated_image.append(pygame.transform.rotate(original_icon, i))
        return rotated_image

def load_animated_spin_animations(screen, icon_center_x, icon_center_y, frame_index, rotated_roulette_wheel, animation_speed):
    frame_index += animation_speed
    frame_index %= len(rotated_roulette_wheel)
    image = rotated_roulette_wheel[int(frame_index)]
    rect = image.get_rect(center=(icon_center_x, icon_center_y))
    screen.blit(image, rect)
    return frame_index

def draw_apartment(screen, mouse_pos, screen_width, screen_height, font, clock, events, apartment, current_renting_expenses, apartment_index = 0):
    day, month, year = utils.date_time_timer()
    fps = 60
    line_spacing = 5

    fps_rect_width = screen_width / 11.67
    fps_rect_height = screen_height / 30
    fps_rect_position_x = screen_width / 140
    fps_rect_position_y = screen_height / 1.05

    exit_door_icon_path = "assets\\icons\\door_icon.webp"
    exit_door_icon_width = screen_width / 23
    exit_door_icon_height = screen_height / 9
    exit_door_icon_position_x = screen_width / 1.05
    exit_door_icon_position_y = screen_height / 1.12

    inventory_icon_width = screen_width / 8
    inventory_icon_height = screen_height / 15
    inventory_icon_position_x = screen_width / 1.2173913043 
    inventory_icon_position_y = screen_height / 60 

    real_estate_button_rect = None 
    inventory_icon_rect = None

    if apartment_index == 0:
        real_estate_button_width = screen_width / 7
        real_estate_button_height = screen_height / 20
        real_estate_button_position_x = screen_width / 1.2068965517 - real_estate_button_width - screen_width / 70
        real_estate_button_position_y = screen_height / 50

        fps_rect = pygame.Rect(fps_rect_position_x, fps_rect_position_y, fps_rect_width, fps_rect_height)

        calendar_rect = pygame.Rect(20, 10, screen_width, 50)

        text_rect = pygame.Rect(10, 50, screen_width, 300)
        real_estate_button_rect = pygame.Rect(real_estate_button_position_x, real_estate_button_position_y, real_estate_button_width, real_estate_button_height)
        inventory_icon_rect = const.inventory_button 

        load_background_image(screen, "assets\\background_photos\\home_background_1.png")
        draw_text(screen, text_messages.game_screen1_text + f"{const.balance} dollars, your salary is {const.salary}, and your total apartment expenses are {current_renting_expenses}", const.black, text_rect, font, line_spacing=5)
        draw_text(screen, f"Date: {day}, {str(const.day_counter)} of {month}, {year}", const.black, calendar_rect, font, line_spacing=5)

        icon_position_x, icon_position_y, icon_width, icon_height = load_icons(const.screen, "assets\\icons\\settings_icon_2.png", const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_SETTINGS)

        icon_position_x, icon_position_y,  icon_width, icon_height = load_icons(const.screen, exit_door_icon_path, exit_door_icon_width, exit_door_icon_height, exit_door_icon_position_x, exit_door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        draw_button(screen, const.blue, const.inventory_button, "Inventory", font, const.black, mouse_pos)
        draw_button(screen, const.blue, real_estate_button_rect, "Real estate", font, const.black, mouse_pos)

        if const.fps_show: 
            show_fps_counter(screen, clock, const.black, fps_rect, font, fps, line_spacing)
    
    if apartment_index == 1 or apartment_index == 2:

        real_estate_icon_path = "assets\\icons\\apartment_icons\\real_estate_icon_2.png"
        real_estate_icon_width = screen_width / 7
        real_estate_icon_height = screen_height / 15
        real_estate_icon_position_x = screen_width / 1.8181818182 
        real_estate_icon_position_y = screen_height / 1.0909090909 

        inventory_icon_path = "assets\\icons\\apartment_icons\\inventory_icon_2.png"

        fps_rect = pygame.Rect(fps_rect_position_x, fps_rect_position_y, fps_rect_width, fps_rect_height)

        calendar_rect = pygame.Rect(20, 10, screen_width, 50)

        text_rect = pygame.Rect(10, 50, screen_width, 300)

        if apartment_index == 2:
            load_background_image(screen, "assets\\background_photos\\home_background_3.png")
            icon_position_x, icon_position_y, icon_width, icon_height = load_icons(const.screen, "assets\\icons\\settings_icon.png", const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        if apartment_index == 1:
            load_background_image(screen, "assets\\background_photos\\home_background_2.png")
            icon_position_x, icon_position_y, icon_width, icon_height = load_icons(const.screen, "assets\\icons\\settings_icon_2.png", const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_SETTINGS)
        draw_text(screen, text_messages.game_screen1_text + f"{const.balance} dollars, your salary is {const.salary}, and your total apartment renting expenses are {current_renting_expenses}", const.white, text_rect, font, line_spacing=5)
        draw_text(screen, f"Date: {day}, {str(const.day_counter)} of {month}, {year}", const.white, calendar_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = load_icons(const.screen, exit_door_icon_path, exit_door_icon_width, exit_door_icon_height, exit_door_icon_position_x, exit_door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        load_icons(screen, real_estate_icon_path, real_estate_icon_width, real_estate_icon_height, real_estate_icon_position_x, real_estate_icon_position_y)
        load_icons(screen, inventory_icon_path, inventory_icon_width, inventory_icon_height, inventory_icon_position_x, inventory_icon_position_y)

        if const.fps_show: 
            show_fps_counter(const.screen, clock, const.black, fps_rect, font, fps, line_spacing)

        real_estate_button_rect = pygame.Rect(real_estate_icon_position_x, real_estate_icon_position_y, real_estate_icon_width, real_estate_icon_height)
        inventory_icon_rect = pygame.Rect(inventory_icon_position_x, inventory_icon_position_y, inventory_icon_width, inventory_icon_height)

    if apartment_index == 3:
        fps_icon_path = "assets\\icons\\fps_icon.png"
        fps_icon_width = screen_width / 8.4848484848484848484848484848485
        fps_icon_height = screen_height / 17.142857142857142857142857142857 
        fps_icon_position_x = screen_width / 140 
        fps_icon_position_y = screen_height / 1.07 

        fps_rect_width = screen_width / 11.67
        fps_rect_height = screen_height / 30
        fps_rect_position_x = fps_icon_position_x + fps_icon_width / 3.6666666667
        fps_rect_position_y = fps_icon_position_y + fps_icon_height / 3.5

        relaxing_at_home_icon_path = "assets\\icons\\apartment_icons\\relaxing_at_home_apartment_icon.png"
        relaxing_at_home_icon_width = screen_width / 5
        relaxing_at_home_icon_height = screen_height / 9
        relaxing_at_home_icon_position_x = screen_width / 2 - relaxing_at_home_icon_width / 2
        relaxing_at_home_icon_position_y = screen_height / 30

        exit_door_icon_path = "assets\\icons\\apartment_icons\\exit_door_icon.png"
        exit_door_icon_width = screen_width / 28
        exit_door_icon_height = screen_height / 10
        exit_door_icon_position_x = screen_width / 1.05
        exit_door_icon_position_y = screen_height / 1.12

        real_estate_icon_path = "assets\\icons\\apartment_icons\\real_estate_icon.png"
        real_estate_icon_width = screen_width / 7
        real_estate_icon_height = screen_height / 15
        real_estate_icon_position_x = screen_width / 2.1538461538 
        real_estate_icon_position_y = screen_height / 1.0909090909 

        watch_tv_icon_path = "assets\\icons\\apartment_icons\\watch_tv_icon.png" 
        watch_tv_icon_width = screen_width / 7.5
        watch_tv_icon_height = screen_height / 15
        watch_tv_icon_position_x = screen_width / 2.1538461538
        watch_tv_icon_position_y = screen_height / 1.8181818182

        sleep_icon_path = "assets\\icons\\apartment_icons\\sleep_icon.png"
        sleep_icon_width = screen_width / 8
        sleep_icon_height = screen_height / 15
        sleep_icon_position_x = screen_width / 1.3861386139
        sleep_icon_position_y = screen_height / 1.8181818182

        relax_icon_path = "assets\\icons\\apartment_icons\\relax_icon.png"
        relax_icon_width = screen_width / 8
        relax_icon_height = screen_height / 15
        relax_icon_position_x = screen_width / 5.6
        relax_icon_position_y = screen_height / 1.3333333333

        info_bckgd_icon_path = "assets\\icons\\apartment_icons\\info_background_icon.png"
        info_bckgd_icon_width = screen_width / 4.6666666667
        info_bckgd_icon_height = screen_height / 4
        info_bckgd_icon_position_x = 2
        info_bckgd_icon_position_y = 2

        calendar_icon_path = "assets\\icons\\apartment_icons\\calendar_icon.png"
        calendar_icon_width = info_bckgd_icon_width / 15
        calendar_icon_height = info_bckgd_icon_height / 8.5
        calendar_icon_position_x = info_bckgd_icon_position_x + info_bckgd_icon_width / 10
        calendar_icon_position_y = info_bckgd_icon_position_y + info_bckgd_icon_height / 6.5

        balance_icon_path = "assets\\icons\\apartment_icons\\balance_icon.png"
        balance_icon_width = info_bckgd_icon_width / 15
        balance_icon_height = info_bckgd_icon_height / 7.5
        balance_icon_position_x = calendar_icon_position_x
        balance_icon_position_y = calendar_icon_position_y + calendar_icon_height + info_bckgd_icon_height / 15

        salary_icon_path = "assets\\icons\\apartment_icons\\salary_icon.png"
        salary_icon_width = info_bckgd_icon_width / 15
        salary_icon_height = info_bckgd_icon_height / 7.5
        salary_icon_position_x = calendar_icon_position_x
        salary_icon_position_y = balance_icon_position_y + balance_icon_height + info_bckgd_icon_height / 15

        rent_icon_path = "assets\\icons\\apartment_icons\\rent_icon.png"
        rent_icon_width = info_bckgd_icon_width / 15
        rent_icon_height = info_bckgd_icon_height / 7.5
        rent_icon_position_x = calendar_icon_position_x
        rent_icon_position_y = salary_icon_position_y + salary_icon_height + info_bckgd_icon_height / 15

        inventory_icon_path = "assets\\icons\\apartment_icons\\inventory_icon.png"

        load_background_image(screen, "assets\\background_photos\\home_background_4.png")
        icon_position_x, icon_position_y,  icon_width, icon_height = load_icons(const.screen, exit_door_icon_path, exit_door_icon_width, exit_door_icon_height, exit_door_icon_position_x, exit_door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
        icon_position_x, icon_position_y, icon_width, icon_height = load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)

        load_icons(const.screen, fps_icon_path, fps_icon_width, fps_icon_height, fps_icon_position_x, fps_icon_position_y)
        load_icons(const.screen, relaxing_at_home_icon_path, relaxing_at_home_icon_width, relaxing_at_home_icon_height, relaxing_at_home_icon_position_x, relaxing_at_home_icon_position_y)
        load_icons(const.screen, real_estate_icon_path, real_estate_icon_width, real_estate_icon_height, real_estate_icon_position_x, real_estate_icon_position_y)
        load_icons(const.screen, watch_tv_icon_path, watch_tv_icon_width, watch_tv_icon_height, watch_tv_icon_position_x, watch_tv_icon_position_y)
        load_icons(const.screen, sleep_icon_path, sleep_icon_width, sleep_icon_height, sleep_icon_position_x, sleep_icon_position_y)
        load_icons(const.screen, relax_icon_path, relax_icon_width, relax_icon_height, relax_icon_position_x, relax_icon_position_y)
        load_icons(const.screen, info_bckgd_icon_path, info_bckgd_icon_width, info_bckgd_icon_height, info_bckgd_icon_position_x, info_bckgd_icon_position_y)
        load_icons(const.screen, calendar_icon_path, calendar_icon_width, calendar_icon_height, calendar_icon_position_x, calendar_icon_position_y)
        load_icons(const.screen, balance_icon_path, balance_icon_width, balance_icon_height, balance_icon_position_x, balance_icon_position_y)
        load_icons(const.screen, salary_icon_path, salary_icon_width, salary_icon_height, salary_icon_position_x, salary_icon_position_y)
        load_icons(const.screen, rent_icon_path, rent_icon_width, rent_icon_height, rent_icon_position_x, rent_icon_position_y)
        load_icons(const.screen, inventory_icon_path, inventory_icon_width, inventory_icon_height, inventory_icon_position_x, inventory_icon_position_y)

        font = pygame.font.SysFont(None, 20)
        calendar_text_rect = pygame.Rect(calendar_icon_position_x + calendar_icon_width + calendar_icon_width / 5, calendar_icon_position_y + (calendar_icon_height - font.get_height()) / 2, info_bckgd_icon_width, calendar_icon_height)
        draw_text(screen, f"Date: {day}, {str(const.day_counter)} of {month}, {year}", const.golden_settings_button, calendar_text_rect, font, line_spacing=5)
        balance_text_rect = pygame.Rect(balance_icon_position_x + balance_icon_width + balance_icon_width / 5, balance_icon_position_y + (balance_icon_height - font.get_height()) / 2, info_bckgd_icon_width, balance_icon_height)
        draw_text(screen, f"Balance: {const.balance}$", const.golden_settings_button, balance_text_rect, font, line_spacing=5)
        salary_text_rect = pygame.Rect(salary_icon_position_x + salary_icon_width + salary_icon_width / 5, salary_icon_position_y + (salary_icon_height - font.get_height()) / 2, info_bckgd_icon_width, salary_icon_height)
        draw_text(screen, f"Salary: {const.salary}", const.golden_settings_button, salary_text_rect, font, line_spacing=5)
        rent_text_rect = pygame.Rect(rent_icon_position_x + rent_icon_width + rent_icon_width / 5, rent_icon_position_y + (rent_icon_height - font.get_height()) / 2, info_bckgd_icon_width, rent_icon_height)
        draw_text(screen, f"Rent expenses: {current_renting_expenses}", const.golden_settings_button, rent_text_rect, font, line_spacing=5)

        fps_rect = pygame.Rect(fps_rect_position_x, fps_rect_position_y, fps_rect_width, fps_rect_height)

        if const.fps_show: 
            show_fps_counter(const.screen, clock, const.golden_settings_button, fps_rect, font, fps, line_spacing)

        real_estate_button_rect = pygame.Rect(real_estate_icon_position_x, real_estate_icon_position_y, real_estate_icon_width, real_estate_icon_height)
        inventory_icon_rect = pygame.Rect(inventory_icon_position_x, inventory_icon_position_y, inventory_icon_width, inventory_icon_height)

    return real_estate_button_rect, inventory_icon_rect