import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def shopping_center_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 6
    icon_width_screen = const.screen.get_width() / 3 - position_x - position_x / 3
    icon_height_screen = const.screen.get_height() / 3
    info_text = "Balance:" + str(const.balance)
    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        utils.play_music()

        const.screen.fill(const.store_bckgd)

        draw_functions.draw_title(const.screen, const.store_text, "STORE")
        draw_functions.draw_text(const.screen, info_text, const.black, const.text_rect, font,line_spacing=5)
        
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_cars_icon.png", icon_width_screen, icon_height_screen, position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CARS)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_electronics_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width + position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_ELECTRONICS)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_furniture_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_FURNITURE)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_clothing_icon.png", icon_width_screen, icon_height_screen, position_x, position_y + icon_height_screen + position_y / 2)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CLOTHING)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_tools_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y + icon_height_screen + position_y / 2)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TOOLS)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_center_groceries_icon.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y + icon_height_screen + position_y / 2)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_GROCERIES)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)
        
        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, const.fps_rect, font, const.fps, const.line_spacing)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)