import pygame
import city_screen
import draw_functions
import apartment_screen
import const
import casino_screen
import work_screen

def get_icon_rect_and_handle_click(position_x, position_y, icon_width, icon_height, type):
    icon_rect = pygame.Rect(position_x, position_y,  icon_width, icon_height)
    handle_icon_click(icon_rect, type)

def handle_icon_click(icon_rect, type):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if icon_rect.collidepoint(mouse_pos) and type == "casino":
        if(mouse_click[0]):
            casino_screen.casino_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "apartment":
        if(mouse_click[0]):
            apartment_screen.apartment_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "exit_door":
        if(mouse_click[0]):
            city_screen.city_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "work":
        if(mouse_click[0]):
            work_screen.work_screen()
    
