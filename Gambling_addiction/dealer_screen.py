import pygame
import const
import draw_functions
import utils
import sys

def dealer_screen():
    running = True
    pygame.font.init()

    while running:
        const.screen.fill(const.white)

        draw_functions.load_background_image(const.screen, "background_photos\janitor_screen_background.png")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, const.screen.get_width()-100, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
        
        running = utils.handle_quit(running)
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)