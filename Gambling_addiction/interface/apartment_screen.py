import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
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
    draw_inventory = False
    next_button_rect = pygame.Rect(0, 0, 0, 0)
    use_button_rect = pygame.Rect(0, 0, 0, 0)
    product = None

    clock = pygame.time.Clock()
    
    while running:
        inventory_length = len(const.inventory_list)
        events = pygame.event.get()

        draw_functions.load_background_image(const.screen, "background_photos\\home_background.png")
        draw_functions.draw_text(const.screen, text_messages.game_screen1_text + f"{const.balance} dollars, and your salary is {const.salary}", const.black, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
       
        day, month, year = utils.date_time_timer()
        draw_functions.draw_text(const.screen, f"Date: {day}, {month}, {year}", const.black, calendar_rect, font, line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        draw_functions.draw_button(const.screen, const.blue, const.inventory_button, "Inventory", font, const.black, mouse_pos)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y - 10)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)

        if inventory_length > 0:
            product = const.inventory_list[const.inventory_index]

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if const.inventory_button.collidepoint(mouse_pos):
                    draw_inventory = not draw_inventory
                if next_button_rect.collidepoint(mouse_pos):
                    if const.inventory_index == inventory_length - 1:
                        const.inventory_index = 0
                    elif const.inventory_index < inventory_length - 1:
                        const.inventory_index += 1
                if use_button_rect.collidepoint(mouse_pos) and inventory_length > 0:
                    utils.use_inventory_item(product)
            
        if draw_inventory and inventory_length > 0:
           next_button_rect, use_button_rect = draw_functions.draw_inventory_card(const.screen, product)
        elif draw_inventory and inventory_length <= 0:
            next_button_rect, use_button_rect = draw_functions.draw_inventory_card(const.screen)

        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, pygame.Rect(10, 570, 130, 20), font, 60, 5)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)