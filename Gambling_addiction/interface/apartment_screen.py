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
    rect_list_inventory = {}
    rect_list_apartment = {}
    day = 0
    month = " "
    year = " "
    month_old = " "
    x_coordinate = 0
    y_coordinate = 0
    const.real_estate_list = []

    inventory_buttons = [("Use", "Use"), ("right", "->")]
    real_estate_buttons = [("left", "<-"), ("rent", "Rent"), ("buy", "Buy"), ("right", "->")]
    real_estate_buttons_when_renting = [("left", "<-"), ("rent", "Rent"), ("buy", "Buy"), ("stop renting", "Stop renting"), ("right", "->")]

    clock = pygame.time.Clock() 

    tier_1_apartment = apartment_class.apartment(0, 100000, 300, "assets\\icons\\apartment_icons\\tier_1_apartment.png", True, False, 400, 300)
    const.real_estate_list.append(tier_1_apartment)
    tier_2_apartment = apartment_class.apartment(1, 500000, 1500, "assets\\icons\\apartment_icons\\tier_2_apartment.png", False, False, 2000, 1500)
    const.real_estate_list.append(tier_2_apartment)
    tier_3_apartment = apartment_class.apartment(2, 2000000, 6000, "assets\\icons\\apartment_icons\\tier_3_apartment.png", False, False, 8000, 7000)
    const.real_estate_list.append(tier_3_apartment)
    tier_4_apartment = apartment_class.apartment(3, 10000000, 30000, "assets\\icons\\apartment_icons\\tier_4_apartment.png", False, False, 40000, 35000)
    const.real_estate_list.append(tier_4_apartment)

    day, month_old, year = utils.date_time_timer()
    real_estate_card_surface = None
    inventory_card_surface = None
    inventory_length = 0

    while running:
        inventory_length = len(const.inventory_list)
        real_estate_list_length = len(const.real_estate_list)
        events = pygame.event.get()
        sound_settings.play_music()
        mouse_pos = pygame.mouse.get_pos()
        day, month, year = utils.date_time_timer()

        if month != month_old:
            const.balance -= const.renting_apartment[0].renting_expenses
            month_old = month

        real_estate_button_rect, inventory_button_rect = draw_functions.draw_apartment(const.screen, mouse_pos, screen_width, screen_height, font, clock, events, const.renting_apartment[0], const.renting_apartment[0].renting_expenses, const.renting_apartment[0].index)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inventory_button_rect.collidepoint(mouse_pos):
                    draw_inventory = not draw_inventory
                    if not draw_inventory:
                        inventory_card_surface = None
                if len(rect_list_inventory) > 0 :
                    if rect_list_inventory["right"].collidepoint(mouse_pos):
                        if const.inventory_index == inventory_length - 1:
                            const.inventory_index = 0
                        elif const.inventory_index < inventory_length - 1:
                            const.inventory_index += 1
                        inventory_card_surface = None
                    if rect_list_inventory["Use"].collidepoint(mouse_pos) and inventory_length > 0:
                        utils.use_inventory_item(product)
                        inventory_card_surface = None
                        inventory_length = len(const.inventory_list)
                if real_estate_button_rect.collidepoint(mouse_pos):
                    draw_apartment_list = not draw_apartment_list
                    if not draw_apartment_list:
                        real_estate_card_surface = None
                if len(rect_list_apartment) > 0:
                    if rect_list_apartment["left"].collidepoint(mouse_pos):
                        if const.real_estate_index > 0:
                            const.real_estate_index -= 1
                        else:
                            const.real_estate_index = 0
                        real_estate_card_surface = None
                    if rect_list_apartment["rent"].collidepoint(mouse_pos): #Rent
                        if const.balance < apartment.rent_price:
                            draw_functions.draw_message_box("Not enough money", "You don't have enough money to rent this apartment!")
                        else:
                            for i in const.real_estate_list:
                                if i.index != apartment.index:
                                    i.renting_apartment = False
                            draw_functions.draw_message_box("Welcome", "Welcome to your new apartment!")
                            const.renting_apartment.clear()
                            apartment.renting_apartment = True
                            const.renting_apartment.append(apartment)
                            real_estate_card_surface = None
                            utils.update_apartment_file()
                            const.balance -= const.renting_apartment[0].renting_expenses
                            const.renting_apartment_index = const.renting_apartment[0].index
                            draw_apartment_list = False
                    if rect_list_apartment["buy"].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 2", "") #Buy
                    if "stop renting" in rect_list_apartment:
                        if rect_list_apartment["stop renting"].collidepoint(mouse_pos):
                            draw_functions.draw_message_box("Button stop renting", "") #stop renting
                    if rect_list_apartment["right"].collidepoint(mouse_pos):

                        if const.real_estate_index >= real_estate_list_length - 1:
                            const.real_estate_index = real_estate_list_length - 1
                        else:
                            const.real_estate_index += 1
                        real_estate_card_surface = None

        if inventory_length > 0:
            product = const.inventory_list[const.inventory_index]
        
        if real_estate_list_length > 0:
            apartment = const.real_estate_list[const.real_estate_index]

        if draw_inventory and inventory_length > 0 and inventory_card_surface is None:
            inventory_card_surface, rect_list_inventory, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, inventory_buttons, product)
            draw_apartment_list = False
            real_estate_card_surface = None
        elif draw_inventory and inventory_length <= 0 and inventory_card_surface is None:
            inventory_card_surface, rect_list_inventory, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, inventory_buttons)
            draw_apartment_list = False
            real_estate_card_surface = None
        
        if draw_apartment_list and not apartment.index == const.renting_apartment[0].index and real_estate_card_surface is None:
            real_estate_card_surface, rect_list_apartment, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, real_estate_buttons, apartment) #draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, real_estate_buttons, apartment)
            draw_inventory = False
            inventory_card_surface = None
            rect_list_inventory.clear()
        elif draw_apartment_list and apartment.index == const.renting_apartment[0].index and real_estate_card_surface is None:
            real_estate_card_surface, rect_list_apartment, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, real_estate_buttons_when_renting, apartment) #draw_functions.draw_card(const.screen, const.job_button, const.job_cards_text, real_estate_buttons, apartment)
            draw_inventory = False
            inventory_card_surface = None
            rect_list_inventory.clear()

        if real_estate_card_surface is not None:
            const.screen.blit(real_estate_card_surface, (x_coordinate, y_coordinate))

        if inventory_card_surface is not None:
            const.screen.blit(inventory_card_surface, (x_coordinate, y_coordinate))

        if not draw_inventory and inventory_card_surface is None:
            rect_list_inventory.clear()
        if not draw_apartment_list and real_estate_card_surface is None:
            rect_list_apartment.clear()

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)