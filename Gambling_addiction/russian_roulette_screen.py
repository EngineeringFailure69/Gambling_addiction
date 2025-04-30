import pygame
import const
import draw_functions
import utils
import city_screen

def russian_roulette_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\game_russian_roulette_background.png")
        
        running = utils.handle_quit(running)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, 1100, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_EXIT_APARTMENT)
       
        pygame.display.flip()
    pygame.quit()
    exit()