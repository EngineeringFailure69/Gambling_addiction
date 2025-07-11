import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def beds_section_screen():
    running = True
    pygame.font.init()
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(10, const.screen.get_height() / 17, screen_width, 300)
    info_text = "Balance:" + str(const.balance)
    font = pygame.font.SysFont(None, 30)

    while running:
        events = pygame.event.get()

        const.screen.fill(const.store_bckgd)

        draw_functions.draw_title(const.screen, const.store_text, "BEDS SECTION")
        draw_functions.draw_text(const.screen, info_text, const.black, text_rect, font,line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\furniture_section_icon.svg", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_FURNITURE)
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)