import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages

def dealer_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    text_rect = pygame.Rect(10, 100, const.screen.get_width(), 300)

    draw_functions.load_background_image(const.screen, "background_photos\\dealer_screen_background.png")
    draw_functions.draw_title(const.screen, const.white, "DEALER POSITION")
    draw_functions.draw_text(const.screen, text_messages.dealer_job_description, const.white, text_rect, font, line_spacing=5)

    while running:
        events = pygame.event.get()

        mouse_pos = pygame.mouse.get_pos()

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.work_icon_path, const.work_icon_width, const.work_icon_height, const.work_icon_position_x, const.work_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        draw_functions.draw_button(const.screen, const.blue, const.apply_button, "Apply", font, const.white, mouse_pos)
        utils.job_apply(const.apply_button, 3500, 1095, "dealer")
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)