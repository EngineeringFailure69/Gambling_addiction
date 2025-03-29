import pygame
import sys
import os
import sys
import importlib.util
import os
import draw_functions
import const
import gambling_addiction
import game_screen1 

def main_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, 100, screen_width, 300)

    while running:
        const.screen.fill(const.white)
        draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        draw_functions.draw_text(const.screen, const.start_screen_info, const.black, text_rect, font, line_spacing=5)

        Start_button = pygame.Rect(const.screen.get_width()-750, const.screen.get_height()-300, const.button_width, const.button_height)
        Quit_button = pygame.Rect(const.screen.get_width()-750, const.screen.get_height()-150, const.button_width, const.button_height)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        start_colour, quit_colour = draw_functions.change_rect_colour(Start_button, Quit_button, mouse_pos)

        draw_functions.draw_button(const.screen, start_colour, Start_button, "Start", font, const.black)
        draw_functions.draw_button(const.screen, quit_colour, Quit_button, "Quit", font, const.black)

        if Quit_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                pygame.quit()
                exit()
        elif Start_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                game_screen1.game_screen1()

        pygame.display.flip()
    pygame.quit()
    exit()
main_screen()