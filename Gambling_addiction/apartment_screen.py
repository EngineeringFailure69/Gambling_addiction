import pygame
import const
import draw_functions
import utils

def apartment_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(220, 50, screen_width, 300)
    calendar_rect = pygame.Rect(20, 10, screen_width, 50)
    day = ""
    month = ""
    year = 0

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\home_background.png")
        
        running = utils.handle_quit(running)

        draw_functions.draw_text(const.screen, const.game_screen1_text, const.black, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, const.screen.get_width()-100, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
       
        day, month, year = utils.date_time_timer()
        draw_functions.draw_text(const.screen, f"Date: {day}, {month}, {year}", const.black, calendar_rect, font, line_spacing=5)

        utils.update_value_in_file("save_files\information.txt", "day_counter")        
        utils.update_value_in_file("save_files\information.txt", "month_counter")
        utils.update_value_in_file("save_files\information.txt", "year_counter")
        utils.update_value_in_file("save_files\information.txt", "return_day_counter")
        utils.update_value_in_file("save_files\information.txt", "return_month_counter")

        pygame.display.flip()
    pygame.quit()
    exit()