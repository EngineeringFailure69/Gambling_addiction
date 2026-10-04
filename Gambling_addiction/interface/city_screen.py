import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import settings.sound_settings as sound_settings

def city_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    fps = 60
    line_spacing = 5
    fps_rect = pygame.Rect(10, 570, 130, 20)
    clock = pygame.time.Clock()
    action_list = []
  
    while running:
        events = pygame.event.get()
        sound_settings.play_music()

        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "assets\\background_photos\\city_screen_background.png")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\casino_icon.webp", 60, 60, 1030, 50)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_CASINO)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\home_icon.webp", 50, 50, 545, 490)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_APARTMENT)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\work_icon.webp", 50, 50, 1300, 185)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_WORK)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\gun_revolver_icon.svg", 75, 25, 30, 10)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_RUSSIAN_ROULETTE)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icon.svg", 70, 50, 630, 180)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_SHOPPING)
        action_list.append(action)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path_old, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y, icon_width, icon_height, const.STATE_SETTINGS)
        action_list.append(action)

        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.white, fps_rect, font, fps, line_spacing)
        else:
            clock.tick(60)  
              
        action = utils.handle_action_list(action_list, const.STATE_TO_THE_STREETS)
        action_list.clear()
        if action is not None:
            return action 
        
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)