import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import text_messages
import settings.sound_settings as sound_settings

def apartment_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()
    text_rect = pygame.Rect(100, 50, screen_width, 300)
    calendar_rect = pygame.Rect(20, 10, screen_width, 50)
    day = ""
    month = ""
    year = 0
    draw_inventory = False
    draw_apartment_list = False
    product = None
    rect_list_inventory = []
    rect_list_apartment = []

    inventory_number_of_buttons = 2
    real_estate_number_of_buttons = 4

    inventory_buttons_text_list = ["Use", "->"]
    real_estate_buttons_text_list = ["<-", "Rent", "Buy", "->"]

    real_estate_button_width = screen_width / 7
    real_estate_button_height = screen_height / 20
    real_estate_button_position_x = screen_width / 1.2068965517 - real_estate_button_width - screen_width / 70
    real_estate_button_position_y = screen_height / 50

    real_estate_button_rect = pygame.Rect(real_estate_button_position_x, real_estate_button_position_y, real_estate_button_width, real_estate_button_height)

    fps = 60
    line_spacing = 5
    fps_rect = pygame.Rect(10, 570, 130, 20)
    clock = pygame.time.Clock() 
    while running:
        inventory_length = len(const.inventory_list)
        events = pygame.event.get()
        sound_settings.play_music()

        draw_functions.load_background_image(const.screen, "assets\\background_photos\\home_background_1.png")
        draw_functions.draw_text(const.screen, text_messages.game_screen1_text + f"{const.balance} dollars, and your salary is {const.salary}", const.black, text_rect, font, line_spacing=5)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)
       
        day, month, year = utils.date_time_timer()
        draw_functions.draw_text(const.screen, f"Date: {day}, {month}, {year}", const.black, calendar_rect, font, line_spacing=5)

        mouse_pos = pygame.mouse.get_pos()
        draw_functions.draw_button(const.screen, const.blue, const.inventory_button, "Inventory", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, real_estate_button_rect, "Real estate", font, const.black, mouse_pos)

        icon_position_x, icon_position_y, icon_width, icon_height = draw_functions.load_icons(const.screen, const.settings_icon_path, const.settings_icon_width, const.settings_icon_height, const.settings_icon_position_x, const.settings_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_SETTINGS)

        if inventory_length > 0:
            product = const.inventory_list[const.inventory_index]

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if const.inventory_button.collidepoint(mouse_pos):
                    draw_inventory = not draw_inventory
                if len(rect_list_inventory) > 0 :
                    if rect_list_inventory[1].collidepoint(mouse_pos):
                        if const.inventory_index == inventory_length - 1:
                            const.inventory_index = 0
                        elif const.inventory_index < inventory_length - 1:
                            const.inventory_index += 1
                    if rect_list_inventory[0].collidepoint(mouse_pos) and inventory_length > 0:
                        utils.use_inventory_item(product)
                if real_estate_button_rect.collidepoint(mouse_pos):
                    draw_apartment_list = not draw_apartment_list
                if len(rect_list_apartment) > 0:
                    if rect_list_apartment[0].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 0", "") #<-
                    if rect_list_apartment[1].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 1", "") #Rent
                    if rect_list_apartment[2].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 2", "") #Buy
                    if rect_list_apartment[3].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 3", "") #->
    
        if draw_inventory and inventory_length > 0:
            rect_list_inventory = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, inventory_number_of_buttons, inventory_buttons_text_list, product)
            draw_apartment_list = False
        elif draw_inventory and inventory_length <= 0:
            rect_list_inventory = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, inventory_number_of_buttons, inventory_buttons_text_list)
            draw_apartment_list = False
        
        if draw_apartment_list:
            rect_list_apartment = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, real_estate_number_of_buttons, real_estate_buttons_text_list)
            draw_inventory = False

        if not draw_inventory:
            rect_list_inventory.clear()
        if not draw_apartment_list:
            rect_list_apartment.clear()

        if const.fps_show: 
            draw_functions.show_fps_counter(const.screen, clock, const.black, fps_rect, font, fps, line_spacing)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)