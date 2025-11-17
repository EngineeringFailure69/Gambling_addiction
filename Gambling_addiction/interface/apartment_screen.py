import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import utils.file_utils as file_utils
import sys
import text_messages

def apartment_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(100, 50, screen_width, 300)
    calendar_rect = pygame.Rect(20, 10, screen_width, 50)
    day = ""
    month = ""
    year = 0

    while running:
        events = pygame.event.get()

        draw_functions.load_background_image(const.screen, "background_photos\\home_background.png")
        draw_functions.draw_text(const.screen, text_messages.game_screen1_text + f"{const.balance} dollars, and your salary is {const.salary}", const.black, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
       
        day, month, year = utils.date_time_timer()
        draw_functions.draw_text(const.screen, f"Date: {day}, {month}, {year}", const.black, calendar_rect, font, line_spacing=5)

        file_utils.update_value_in_file("save_files\\information.txt", "day_counter")        
        file_utils.update_value_in_file("save_files\\information.txt", "month_counter")
        file_utils.update_value_in_file("save_files\\information.txt", "year_counter")
        file_utils.update_value_in_file("save_files\\information.txt", "return_day_counter")
        file_utils.update_value_in_file("save_files\\information.txt", "return_month_counter")

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)