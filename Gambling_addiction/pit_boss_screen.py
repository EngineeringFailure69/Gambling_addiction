import pygame
import const
import draw_functions
import utils
import sys
import text_messages

def pit_boss_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    text_rect = pygame.Rect(10, 100, const.screen.get_width(), 300)

    while running:
        const.screen.fill(const.white)

        draw_functions.load_background_image(const.screen, "background_photos\pit_boss_screen_background.png")

        draw_functions.draw_title(const.screen, const.white, "PIT BOSS POSITION")

        draw_functions.draw_text(const.screen, text_messages.pit_boss_job_position, const.white, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, const.screen.get_width()-100, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
        
        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\work_icon.webp", 70, 70, const.screen.get_width()/47, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        draw_functions.draw_button(const.screen, const.blue, const.apply_button, "Apply", font, const.white)
        utils.job_apply(const.apply_button, 6000, 25, "pit boss")

        running = utils.handle_quit(running)
       
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)