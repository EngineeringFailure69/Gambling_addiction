import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def fruits_section_screen():
    running = True
    pygame.font.init()
    position_x = const.screen.get_width() / 18
    position_y = const.screen.get_height() / 4
    icon_width_screen = const.screen.get_width() / 4 - position_x - position_x / 4
    icon_height_screen = const.screen.get_height() / 2
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, const.screen.get_height() / 17, screen_width, 300)
    info_text = "Balance:" + str(const.balance)
    font = pygame.font.SysFont(None, 30)

    while running:
        events = pygame.event.get()

        const.screen.fill(const.fruit_bckg)

        draw_functions.draw_title(const.screen, const.store_text, "FRUITS SECTION")
        draw_functions.draw_text(const.screen, info_text, const.black, text_rect, font,line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\groceries_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_GROCERIES)
       
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\fruit_icon_1.png", icon_width_screen, icon_height_screen, position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, True, 1.50)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\fruit_icon_2.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, True, 2.20)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\fruit_icon_3.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, True, 1.80)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\fruit_icon_4.png", icon_width_screen, icon_height_screen, position_x + icon_width_screen + position_x + icon_width_screen + position_x + icon_width_screen + position_x, position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_BUY_PRODUCT, True, 1.90)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\door_icon.webp", 75, 75, const.screen.get_width()-80, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)