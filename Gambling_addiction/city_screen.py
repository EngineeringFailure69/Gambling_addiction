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

        # mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\casino_icon.webp", 100, 100, 605, 160)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_CASINO)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\home_icon.webp", 50, 50, 970, 230)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_APARTMENT)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\work_icon.webp", 100, 100, 615, 430)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_WORK)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\gun_revolver.png", 100, 35, 355, 185)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_RUSSIAN_ROULETTE)

        running = utils.handle_quit(running) 
       
        pygame.display.flip()
    pygame.quit()
    exit()