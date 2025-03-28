import pygame
import sys
import os
import sys
import importlib.util
import os
import draw_functions
import const
import gambling_addiction

def main_screen():
    running = True
    pygame.font.init()
    info = gambling_addiction.return_text()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, 100, screen_width, 300)
    
    while running:
        const.screen.fill(const.white)
        draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        draw_functions.draw_text(const.screen, info, const.black, text_rect, font, line_spacing=5)

        Start_button = pygame.Rect(const.screen.get_width()-750, const.screen.get_height()-300, const.button_width, const.button_height)
        Quit_button = pygame.Rect(const.screen.get_width()-750, const.screen.get_height()-150, const.button_width, const.button_height)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # if Start_button.collidepoint(mouse_pos):
        #    start_colour = const.hover_blue
        # elif Quit_button.collidepoint(mouse_pos):
        #     quit_colour = const.hover_blue
        # else:
        #     start_colour = const.blue
        #     quit_colour = const.blue
        start_colour, quit_colour = draw_functions.change_rect_colour(Start_button, Quit_button, mouse_pos)

        draw_functions.draw_button(const.screen, start_colour, Start_button, "Start", font, const.black)
        draw_functions.draw_button(const.screen, quit_colour, Quit_button, "Quit", font, const.black)

        pygame.display.flip()
    pygame.quit()
    exit()
main_screen()