import pygame
import const
import sys
import os
import utils
from tkinter import *
from tkinter import messagebox

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
    # Kreiraj font objekat
    title_font = pygame.font.Font(None, font_size)

    title_text = text
    title_surface = title_font.render(title_text, True, color)
    title_rect = title_surface.get_rect(center=((screen.get_width() - 50) // 2, screen.get_height() - 550))
    
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
    image = pygame.image.load(resource_path(imagePath))
    scaled_image = pygame.transform.scale(image, (const.screen.get_width(), const.screen.get_height()))
    screen.blit(scaled_image, (0, 0))

def load_icons(screen, imagePath, icon_width, icon_height, icon_position_x, icon_position_y):
    image = pygame.image.load(resource_path(imagePath))
    scaled_image = pygame.transform.scale(image, (icon_width, icon_height))
    screen.blit(scaled_image, (icon_position_x, icon_position_y))
    return icon_position_x, icon_position_y, icon_width, icon_height

def resource_path(relative_path):
    try:
        # Ako je pokrenuto kao .exe, sys._MEIPASS će postojati
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def draw_text_box(screen, colour, rect, text, font, text_color):
        txt_surface = font.render(text, True, text_color)
        pygame.draw.rect(screen, colour, rect, 2)
        const.screen.blit(txt_surface, (rect.x + 5, rect.y + 5))

def format_number(string_number):
    if not string_number:  # Ako je prazan string, vrati prazan string
        return ""
    try:
        number = int(string_number)
    except ValueError:
        return ""
    formatted = f"{number/1000:.3f}" 
    formatted = formatted + "K"
    return formatted