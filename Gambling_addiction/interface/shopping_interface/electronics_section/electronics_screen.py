import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def electronics_screen():
    running = True
    pygame.font.init()

    while running:
        events = pygame.event.get()
        
        const.screen.fill(const.store_bckgd)

        draw_functions.draw_title(const.screen, const.store_text, "ELECTRONICS")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\shopping_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SHOPPING)
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)