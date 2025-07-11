import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def city_screen():
    running = True
    pygame.font.init()

    while running:
        events = pygame.event.get()

        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\\city_screen_background.png")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\casino_icon.webp", 60, 60, 1030, 50)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CASINO)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\home_icon.webp", 50, 50, 545, 490)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_APARTMENT)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\work_icon.webp", 50, 50, 1300, 185)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\gun_revolver_icon.svg", 75, 25, 30, 10)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_RUSSIAN_ROULETTE)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\shopping_icon.svg", 70, 50, 630, 180)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SHOPPING)
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)