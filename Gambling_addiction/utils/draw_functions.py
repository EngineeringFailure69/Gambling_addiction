import pygame
import const
from tkinter import *
from tkinter import messagebox
import utils.file_utils as file_utils

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

def draw_inventory_card(screen, product = None):
    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()
    card_width = 400
    card_height = 500
    x_coordinate = screen_width / 2 - card_width / 2
    y_coordinate = screen_height / 1.8 - card_height / 2 
    button_width = 160
    button_height = 40
    icon_width = card_width - 40
    icon_height = 400
    button_font_size = 30
    button_font_size = pygame.font.SysFont(None, button_font_size, bold = False)
    pygame.draw.rect(screen, const.job_box, pygame.Rect(x_coordinate, y_coordinate, card_width, card_height))
    next_button_rect = pygame.Rect(x_coordinate + card_width / 2 + 20, card_height + 30, button_width, button_height)
    use_button_rect = pygame.Rect(x_coordinate + 20, card_height + 30, button_width, button_height)
    draw_button(screen, const.job_button, next_button_rect, "->", button_font_size, const.job_cards_text)
    draw_button(screen, const.job_button, use_button_rect, "Use", button_font_size, const.job_cards_text)
    if product != None:
        load_icons(const.screen, product.image_path, icon_width, icon_height, x_coordinate + 20, y_coordinate + 20)
    return next_button_rect, use_button_rect

def show_fps_counter(screen, clock, text_colour, text_rect, font, clock_value, line_spacing = 5):
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