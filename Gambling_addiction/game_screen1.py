import pygame
import const
import draw_functions

def game_screen1():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    text_rect = pygame.Rect(125, 10, screen_width, 300)

    while running:
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "apartment_background.png")
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False

        draw_functions.draw_text(const.screen, const.game_screen1_text, const.black, text_rect, font, line_spacing=5)
       
        pygame.display.flip()
    pygame.quit()
    exit()