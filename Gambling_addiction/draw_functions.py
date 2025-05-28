import pygame
import const
from tkinter import *
from tkinter import messagebox
import file_utils

def draw_message_box(title, text):
    #Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo(title, text)

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

def draw_button(surface, colour, rect, text, font, text_color):
    pygame.draw.rect(surface, colour, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)

def draw_title(screen, color, text = "GAMBLING ADDICTION"):
    font_size = 100
    # Create font object
    title_font = pygame.font.Font(None, font_size)

    title_text = text
    title_surface = title_font.render(title_text, True, color)
    title_rect = title_surface.get_rect(center=((screen.get_width() - 50) // 2, screen.get_height() / 12))
    
    screen.blit(title_surface, title_rect)

def change_rect_colour(Start_button, Quit_button, mouse_pos):
    start_colour = const.blue
    quit_colour = const.blue
    if Start_button.collidepoint(mouse_pos):
        start_colour = const.hover_blue
    if Quit_button.collidepoint(mouse_pos):
        quit_colour = const.hover_blue
    return start_colour, quit_colour

def load_background_image(screen, imagePath):
    image = pygame.image.load(file_utils.resource_path(imagePath))
    scaled_image = pygame.transform.scale(image, (const.screen.get_width(), const.screen.get_height()))
    screen.blit(scaled_image, (0, 0))

def load_icons(screen, imagePath, icon_width, icon_height, icon_position_x, icon_position_y):
    image = pygame.image.load(file_utils.resource_path(imagePath))
    scaled_image = pygame.transform.scale(image, (icon_width, icon_height))
    screen.blit(scaled_image, (icon_position_x, icon_position_y))
    return icon_position_x, icon_position_y, icon_width, icon_height

def draw_text_box(screen, colour, rect, text, font, text_color):
        txt_surface = font.render(text, True, text_color)
        pygame.draw.rect(screen, colour, rect, 2)
        const.screen.blit(txt_surface, (rect.x + 5, rect.y + 5))

def format_number(string_number):
    if not string_number:  # If the string is empty, return it
        return ""
    try:
        number = int(string_number)
    except ValueError:
        return ""
    if(number<=1000000):
        formatted = f"{number/1000:.3f}" 
        formatted = formatted + "K"
    else:
        formatted = f"{1000000/1000:.3f}" 
        formatted = formatted + "K"
    print(f"Tes broj: {number}")
    return formatted, number

def draw_custom_message_box(screen, text, font):
    box_rect = pygame.Rect(const.screen.get_width()/2-150, const.screen.get_height()/2-25, 300, 50)
    pygame.draw.rect(screen, const.white, box_rect)
    pygame.draw.rect(screen, const.white, box_rect, 3)

    msg_surface = font.render(text, True, const.black)
    msg_rect = msg_surface.get_rect(center=box_rect.center)
    screen.blit(msg_surface, msg_rect)

def draw_info_cards(screen):
    screen_width = const.screen.get_width() #take screen width
    screen_height = const.screen.get_height() #take screen height
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