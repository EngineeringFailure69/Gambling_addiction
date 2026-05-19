import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import settings.sound_settings as sound_settings
import classes.items_class as apartment_class

def apartment_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    screen_width = const.screen.get_width()
    screen_height = const.screen.get_height()
    draw_inventory = False
    draw_apartment_list = False
    product = None
    apartment = None
    rect_list_inventory = []
    rect_list_apartment = []

    inventory_number_of_buttons = 2
    real_estate_number_of_buttons = 4

    inventory_buttons_text_list = ["Use", "->"]
    real_estate_buttons_text_list = ["<-", "Rent", "Buy", "->"]

    clock = pygame.time.Clock() 

    real_estate_index = 0
    real_estate_list = []

    tier_1_apartment = apartment_class.apartment(100000, 300, "assets\\icons\\apartment_icons\\tier_1_apartment.png")
    const.real_estate_list.append(tier_1_apartment)
    tier_2_apartment = apartment_class.apartment(300000, 1000, "assets\\icons\\apartment_icons\\tier_2_apartment.png")
    const.real_estate_list.append(tier_2_apartment)
    tier_3_apartment = apartment_class.apartment(600000, 2000, "assets\\icons\\apartment_icons\\tier_3_apartment.png")
    const.real_estate_list.append(tier_3_apartment)
    tier_4_apartment = apartment_class.apartment(1000000, 3000, "assets\\icons\\apartment_icons\\tier_4_apartment.png")
    const.real_estate_list.append(tier_4_apartment)

    while running:
        inventory_length = len(const.inventory_list)
        real_estate_list_length = len(const.real_estate_list)
        events = pygame.event.get()
        sound_settings.play_music()
        mouse_pos = pygame.mouse.get_pos()

        real_estate_button_rect, inventory_button_rect = draw_functions.draw_apatment(const.screen, mouse_pos, screen_width, screen_height, font, clock, events)

        if inventory_length > 0:
            product = const.inventory_list[const.inventory_index]

        if real_estate_list_length > 0:
            apartment = const.real_estate_list[const.real_estate_index]

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inventory_button_rect.collidepoint(mouse_pos):
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
                        if const.real_estate_index > 0:
                            const.real_estate_index -= 1
                        else:
                            const.real_estate_index = 0
                    if rect_list_apartment[1].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 1", "") #Rent
                    if rect_list_apartment[2].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 2", "") #Buy
                    if rect_list_apartment[3].collidepoint(mouse_pos):
                        if const.real_estate_index >= real_estate_list_length - 1:
                            const.real_estate_index = real_estate_list_length - 1
                        else:
                            const.real_estate_index += 1
    
        if draw_inventory and inventory_length > 0:
            rect_list_inventory = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, inventory_number_of_buttons, inventory_buttons_text_list, product)
            draw_apartment_list = False
        elif draw_inventory and inventory_length <= 0:
            rect_list_inventory = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, inventory_number_of_buttons, inventory_buttons_text_list)
            draw_apartment_list = False
        
        if draw_apartment_list:
            rect_list_apartment = draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, real_estate_number_of_buttons, real_estate_buttons_text_list, apartment)
            draw_inventory = False

        if not draw_inventory:
            rect_list_inventory.clear()
        if not draw_apartment_list:
            rect_list_apartment.clear()

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)