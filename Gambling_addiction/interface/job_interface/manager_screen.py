import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages

def manager_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    text_rect = pygame.Rect(10, 100, const.screen.get_width(), 300)

    draw_functions.load_background_image(const.screen, "background_photos\\manager_screen_background.png")
    draw_functions.draw_title(const.screen, const.white, "MANAGER POSITION")
    draw_functions.draw_text(const.screen, text_messages.manager_job_description, const.white, text_rect, font, line_spacing=5)

    while running:
        events = pygame.event.get()

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\door_icon.webp", 75, 75, const.screen.get_width()-100, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
        
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\work_icon.webp", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        draw_functions.draw_button(const.screen, const.blue, const.apply_button, "Apply", font, const.white)
        utils.job_apply(const.apply_button, 10000, 1095, "manager")
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)