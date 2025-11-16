import pygame
import utils.draw_functions as draw_functions
import const
import interface.apartment_screen as apartment_screen
import utils.utils as utils
import utils.file_utils as file_utils
import sys
import text_messages

def main_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, 100, screen_width, 300)

    const_path = file_utils.resource_path("const.py")
    utils.grab_all_variables(const_path, "STATE")

    Start_button = pygame.Rect(const.screen.get_width()/2-const.button_width/2, const.screen.get_height()-300, const.button_width, const.button_height)
    Quit_button = pygame.Rect(const.screen.get_width()/2-const.button_width/2, const.screen.get_height()-150, const.button_width, const.button_height)

    draw_functions.load_background_image(const.screen, "background_photos\\start_screen_background.png")
    draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

    draw_functions.draw_text(const.screen, text_messages.start_screen_info, const.black, text_rect, font, line_spacing=5)

    while running:
        
        running = utils.handle_quit(running)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed() 

        draw_functions.draw_button(const.screen, const.blue, Start_button, "Start", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, Quit_button, "Quit", font, const.black, mouse_pos)

        if Quit_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                pygame.quit()
                sys.exit(0)
        elif Start_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                apartment_screen.apartment_screen()

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)
main_screen()