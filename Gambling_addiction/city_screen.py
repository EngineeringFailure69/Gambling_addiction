import pygame
import const
import draw_functions
import utils
import apartment_screen

def city_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\city_screen_background.webp")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\casino_icon.webp", 100, 100, 605, 160)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CASINO)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\home_icon.webp", 50, 50, 970, 230)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_APARTMENT)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\work_icon.webp", 100, 100, 615, 430)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
       
        pygame.display.flip()
    pygame.quit()
    exit()