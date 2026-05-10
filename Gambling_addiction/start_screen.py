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
    font = pygame.font.SysFont(None, 60, False, True)
    img_path = "background_photos\\start_screen_background.png"

    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()

    start_button_width = screen_width / 5
    start_button_height = screen_height / 8
    start_button_position_x = screen_width * 0.47
    start_button_position_y = screen_height / 2 - start_button_height 

    quit_button_width = screen_width / 5
    quit_button_height = screen_height / 8
    quit_button_position_x = start_button_position_x
    quit_button_position_y = start_button_position_y + start_button_height + screen_height / 20

    play_button_icon_width = start_button_width / 4.3333333333
    play_button_icon_height = start_button_height / 1.2
    play_button_icon_position_x = start_button_position_x + start_button_width / 28#10
    play_button_icon_position_y = start_button_position_y + (start_button_height - play_button_icon_height)/2
    play_button_icon_path = "icons\\play_button_icon.png"

    quit_button_icon_width = quit_button_width / 4.3333333333
    quit_button_icon_height = quit_button_height / 1.2
    quit_button_icon_position_x = quit_button_position_x + quit_button_width / 28#10
    quit_button_icon_position_y = quit_button_position_y + (quit_button_height - quit_button_icon_height)/2
    quit_button_icon_path = "icons\\quit_button_icon.png"   

    const_path = file_utils.resource_path("const.py")
    utils.grab_all_variables(const_path, "STATE")

    start_button_rect = pygame.Rect(start_button_position_x, start_button_position_y, start_button_width, start_button_height)
    quit_button_rect = pygame.Rect(quit_button_position_x, quit_button_position_y, quit_button_width, quit_button_height)

    icon_center_x = screen_width / 3.4146341463 #410#450
    icon_center_y = screen_height / 1.935483871 #310#290
    animation_icon_path = "icons\\start_screen_roulette_wheel.png"
    icon_width_animation = screen_width / 3.3333333333 #420 #700
    icon_height_animation = screen_height / 1.3953488372 #430 #470
    COUNTER_CLOCK_WISE = True
    angle_increment = 2
    frame_index = 0

    title_icon_path = "icons\\start_screen_title_icon.png"
    title_icon_width = screen_width * 0.6
    title_icon_height = screen_height / 12
    title_icon_position_x = screen_width / 2 - title_icon_width / 2
    title_icon_position_y = screen_height / 17

    clock = pygame.time.Clock()
    utils.play_current_song()

    const.spin_animations = draw_functions.gather_animated_spin_animations(animation_icon_path, icon_width_animation, icon_height_animation, angle_increment, COUNTER_CLOCK_WISE)

    while running:
        events = pygame.event.get()
        utils.change_music_volume()
        utils.play_music()

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed() 

        draw_functions.load_background_image(const.screen, img_path)
        draw_functions.draw_title(const.screen, const.black, "GAMBLING ADDICTION")

        frame_index = draw_functions.load_animated_spin_animations(const.screen, icon_center_x, icon_center_y, frame_index, const.spin_animations, 1)

        if const.fps_show:
            draw_functions.load_icons(const.screen, const.fps_icon_path, const.fps_icon_width, const.fps_icon_height, const.fps_icon_position_x, const.fps_icon_position_y)
            draw_functions.show_fps_counter(const.screen, clock, const.golden_settings_button, const.fps_rect, font, const.fps, const.line_spacing)

        draw_functions.draw_button(const.screen, const.green_settings_button, start_button_rect, "    Start", font, const.golden_settings_button, mouse_pos)
        draw_functions.load_icons(const.screen, play_button_icon_path, play_button_icon_width, play_button_icon_height, play_button_icon_position_x, play_button_icon_position_y)
        draw_functions.draw_button(const.screen, const.green_settings_button, quit_button_rect, "    Quit", font, const.golden_settings_button, mouse_pos)
        draw_functions.load_icons(const.screen, quit_button_icon_path, quit_button_icon_width, quit_button_icon_height, quit_button_icon_position_x, quit_button_icon_position_y)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
 
        draw_functions.load_icons(const.screen, title_icon_path, title_icon_width, title_icon_height, title_icon_position_x, title_icon_position_y)

        if quit_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                pygame.quit()
                sys.exit(0)
        elif start_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                const.spin_animations.clear()
                running = False
                apartment_screen.apartment_screen()

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)
main_screen()