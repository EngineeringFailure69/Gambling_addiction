import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import settings.sound_settings as sound_settings

def electronics_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    info_text = "Balance:" + str(const.balance)
    font = pygame.font.SysFont(None, 30) 

    clock = pygame.time.Clock()
    action_list = []
    while running:
        events = pygame.event.get()
        sound_settings.play_music()
        
        const.screen.fill(const.elecs_bckgd)

        draw_functions.draw_title(const.screen, const.black, "ELECTRONICS")
        draw_functions.draw_text(const.screen, info_text, const.black, const.text_rect, font,line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.shopping_icon_path, const.shopping_icon_width, const.shopping_icon_height, const.shopping_icon_position_x, const.shopping_icon_position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SHOPPING)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icons\\electronics_accessories_icon.png", icon_width_screen, icon_height_screen, position_x, position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_ACCESSORIES)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icons\\electronics_consoles_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CONSOLES)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icons\\electronics_laptops_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_LAPTOPS)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "assets\\icons\\shopping_icons\\electronics_smartphones_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SMARTPHONES)
        action_list.append(action)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
        action_list.append(action)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path_old, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        action = utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
        action_list.append(action)

        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, const.fps_rect, font, const.fps, const.line_spacing)
        else:
            clock.tick(60)
            
        action = utils.handle_action_list(action_list, const.STATE_ELECTRONICS)
        action_list.clear()
        if action is not None:
            return action

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)