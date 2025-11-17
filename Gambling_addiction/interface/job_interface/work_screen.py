import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys

def work_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 70)
    text = "JOB OPENINGS"
    screen_width = const.screen.get_width()
    text_left = screen_width/2 - (5 * 70) / 2
    text_rect = pygame.Rect(text_left, 30, screen_width, 300)

    draw_functions.load_background_image(const.screen, "background_photos\\work_screen_background.png")

    while running:
        events = pygame.event.get()

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        draw_functions.draw_text(const.screen, text, const.black, text_rect, font, line_spacing=5)
        draw_functions.draw_info_cards(const.screen)
        
        utils.job_details()
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)