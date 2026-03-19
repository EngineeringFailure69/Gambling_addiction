import pygame
import utils.draw_functions as draw_functions
import const
import interface.apartment_screen as apartment_screen
import utils.utils as utils
import utils.file_utils as file_utils
import sys

def main_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    img_path = "background_photos\\start_screen_background.png"
    start_button_y = const.screen.get_height()-300
    quit_button_y = const.screen.get_height()-150

    const_path = file_utils.resource_path("const.py")
    utils.grab_all_variables(const_path, "STATE")

    start_button_rect = pygame.Rect(const.button_center_x, start_button_y, const.button_width, const.button_height)
    quit_button_rect = pygame.Rect(const.button_center_x, quit_button_y, const.button_width, const.button_height)

    draw_functions.load_background_image(const.screen, img_path)

    draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

    icon_center_x = 450
    icon_center_y = 290
    icon_path = "icons\\start_screen_roulette_wheel.png"
    icon_width = 700
    icon_height = 470
    angle = 0
    rotated_rect = 0
    angle_increment = 2
    COUNTER_CLOCK_WISE = True

    clock = pygame.time.Clock()
    while running:
        
        running = utils.handle_quit(running)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed() 

        draw_functions.load_background_image(const.screen, img_path)
        draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

        angle, rotated_rect = draw_functions.load_spin_animation(const.screen, icon_center_x, icon_center_y, angle, icon_path, icon_width, icon_height, rotated_rect, angle_increment, COUNTER_CLOCK_WISE)

        draw_functions.draw_button(const.screen, const.blue, start_button_rect, "Start", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, quit_button_rect, "Quit", font, const.black, mouse_pos)

        if quit_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                pygame.quit()
                sys.exit(0)
        elif start_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                apartment_screen.apartment_screen()
            
        fps = clock.get_fps()
        draw_functions.draw_text(const.screen, f"FPS: {round(fps, 2)}", const.white, pygame.Rect(10, 10, 120, 20), font, 5)

        pygame.display.flip()
        clock.tick(160) 
    pygame.quit()
    sys.exit(0)
main_screen()