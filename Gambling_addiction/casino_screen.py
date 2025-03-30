import pygame
import const
import draw_functions
import utils

def casino_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\casino_roulette.jpg")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, 1120, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_EXIT_APARTMENT)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
       
        pygame.display.flip()
    pygame.quit()
    exit()