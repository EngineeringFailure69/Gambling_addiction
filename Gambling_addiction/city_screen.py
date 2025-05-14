import pygame
import const
import draw_functions
import utils
import sys

def city_screen():
    running = True
    pygame.font.init()

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\city_screen_background.png")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\casino_icon.webp", 60, 60, 1030, 50)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CASINO)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\home_icon.webp", 50, 50, 630, 530)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_APARTMENT)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\work_icon.webp", 70, 70, 1250, 220)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\gun_revolver.png", 50, 25, 70, 50)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_RUSSIAN_ROULETTE)

        running = utils.handle_quit(running) 
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)