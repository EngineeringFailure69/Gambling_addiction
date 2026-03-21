import pygame
import const
import sys
import utils.utils as utils
import utils.draw_functions as draw_functions

def settings_screen():
    running = True
    show_fps_button_rect = pygame.Rect(1000, 30, 150, 40)
    back_button_rect = pygame.Rect(700, 30, 150, 40)
    font = pygame.font.SysFont(None, 30)

    while running:
        const.screen.fill(const.white)
        events = pygame.event.get()

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        draw_functions.draw_button(const.screen, const.blue, show_fps_button_rect, "Show fps", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, back_button_rect, "Back", font, const.black, mouse_pos)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and show_fps_button_rect.collidepoint(mouse_pos):
                const.fps_show = not const.fps_show
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(mouse_pos):
                return

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)