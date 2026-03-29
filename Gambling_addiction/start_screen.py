import pygame
import utils.draw_functions as draw_functions
import const
import interface.apartment_screen as apartment_screen
import settings_screen as settings_screen
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

    icon_center_x = 450
    icon_center_y = 290
    animation_icon_path = "icons\\start_screen_roulette_wheel.png"
    icon_width_animation = 700
    icon_height_animation = 470
    COUNTER_CLOCK_WISE = True
    angle = 0
    angle_increment = 2
    rotated_rect = 0

    clock = pygame.time.Clock()
    utils.play_current_song()

    while running:
        events = pygame.event.get()
        utils.play_music(events)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed() 

        draw_functions.load_background_image(const.screen, img_path)
        draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

        angle, rotated_rect = draw_functions.load_spin_animation(const.screen, icon_center_x, icon_center_y, angle, animation_icon_path, icon_width_animation, icon_height_animation, rotated_rect, angle_increment, COUNTER_CLOCK_WISE)

        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.white, const.fps_rect, font, const.fps, const.line_spacing)

        draw_functions.draw_button(const.screen, const.blue, start_button_rect, "Start", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, quit_button_rect, "Quit", font, const.black, mouse_pos)
        
        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
 
        if quit_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                pygame.quit()
                sys.exit(0)
        elif start_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                running = False
                apartment_screen.apartment_screen()

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)
main_screen()