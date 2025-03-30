import pygame
import const
import draw_functions
import utils
import city_screen

def apartment_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(125, 10, screen_width, 300)

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\home_background.png")
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        draw_functions.draw_text(const.screen, const.game_screen1_text, const.black, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, 1100, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_EXIT_APARTMENT)
       
        pygame.display.flip()
    pygame.quit()
    exit()