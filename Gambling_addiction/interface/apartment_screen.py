import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import sys
import settings.sound_settings as sound_settings

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

    inventory_buttons = [("Use", "Use"), ("right", "->")]
    real_estate_buttons = [("left", "<-"), ("rent", "Rent"), ("buy", "Buy"), ("right", "->")]
    real_estate_buttons_when_renting = [("left", "<-"), ("rent", "Rent"), ("buy", "Buy"), ("stop renting", "Stop renting"), ("right", "->")]

    clock = pygame.time.Clock() 

    tier_1_apartment = const.real_estate_list[0]

    day, month_old, year = utils.date_time_timer()
    real_estate_card_surface = None
    inventory_card_surface = None
    inventory_length = 0

    action_list = []

    for real_estate in const.real_estate_list:
        if real_estate.renting_apartment is True:
            current_renting_apartment = real_estate

    while running:
        inventory_length = len(const.inventory_list)
        real_estate_list_length = len(const.real_estate_list)
        events = pygame.event.get()
        sound_settings.play_music()
        mouse_pos = pygame.mouse.get_pos()
        day, month, year = utils.date_time_timer()

        if month != month_old:
            if const.balance >= current_renting_apartment.get_monthly_renting_cost(): #Have money to pay rent
                const.balance -= current_renting_apartment.get_monthly_renting_cost()
                if const.balance > 0 and current_renting_apartment.get_apartment_debt() > 0 and const.balance < current_renting_apartment.get_apartment_debt(): #Have money but not for the entire debt
                    current_renting_apartment.debt -= const.balance
                    const.debt -= const.balance
                    const.balance = 0
                elif const.balance > 0 and current_renting_apartment.get_apartment_debt() > 0 and const.balance >= current_renting_apartment.get_apartment_debt(): #Have money for the entire debt
                    const.balance -= current_renting_apartment.debt
                    current_renting_apartment.debt = 0
                    current_renting_apartment.debt_months_count = 0 #You are no longer in debt, so months and debt are reset
                    const.debt -= current_renting_apartment.debt
                    if const.balance > 0 and const.debt > 0 and const.balance < const.debt: #Not enough money left to pay off the entire debt
                        const.debt -= const.balance
                        const.balance = 0
                    elif const.balance > 0 and const.debt > 0 and const.balance >= const.debt: #Still enough money left to pay off the entire debt
                        const.balance -= const.debt
                        const.debt = 0
            elif const.balance < current_renting_apartment.get_monthly_renting_cost(): #Don't have money to pay rent
                if const.balance > 0: #You have some money but not enough for whole rent
                    current_renting_apartment.debt += (current_renting_apartment.get_monthly_renting_cost() - const.balance) #Give all money you have, and the rest goes to debt
                    current_renting_apartment.debt_months_count += 1 #You are in debt for previous month
                    const.debt += (current_renting_apartment.get_monthly_renting_cost() - const.balance) #Total debt increases
                    const.balance = 0
                elif const.balance == 0:
                    current_renting_apartment.debt += current_renting_apartment.get_monthly_renting_cost() #The entire cost is now debt
                    current_renting_apartment.debt_months_count += 1 #You are in debt for a previous month 
                    const.debt += current_renting_apartment.get_monthly_renting_cost() 

            for real_estate in const.real_estate_list:
                if real_estate.debt_months_count > 3 and real_estate.debt > 0:
                    if const.inventory_list is not None: #If you have something in inventory, stuff get sold for half the original price in order to pay off the debt
                        for item in const.inventory_list:
                            if const.debt > 0 or real_estate.debt > 0:
                                const.balance += item.item_price / 2
                                if const.balance >= real_estate.debt:
                                    const.balance -= real_estate.debt 
                                    const.debt = 0
                                    real_estate.debt = 0
                                elif const.balance < real_estate.debt:
                                    real_estate.debt -= const.balance
                                    const.debt -= const.balance
                                    const.balance = 0
                                utils.remove_item_from_the_inventory(item)
                                draw_functions.draw_message_box("Item sold to pay off debt", f"Your {item.item_type} {item.type} has been sold for {item.item_price / 2} to pay off debt")
                            else: #if you paid off your debt, check stops
                                real_estate.debt_months_count = 0
                                break
            month_old = month

        if current_renting_apartment.debt_months_count > 3 and current_renting_apartment.index > 0: #if your are in debt higher tier apartments over 3 months, you get kicked out
                draw_functions.draw_message_box("Kicked out", "You are kicked out back to tier 1 apartment because you are in debt for over 3 months")
                current_renting_apartment.renting_apartment = False
                current_renting_apartment = tier_1_apartment
                current_renting_apartment.renting_apartment = True

        real_estate_button_rect, inventory_button_rect, exit_door_icon_rect, settings_icon_rect = draw_functions.draw_apartment(const.screen, mouse_pos, screen_width, screen_height, font, clock, events, current_renting_apartment, current_renting_apartment.get_monthly_renting_cost(), current_renting_apartment.index)
        action = utils.get_icon_rect_and_handle_click(events, exit_door_icon_rect.left, exit_door_icon_rect.top, exit_door_icon_rect.width, exit_door_icon_rect.height, const.STATE_TO_THE_STREETS)
        action_list.append(action)
        action = utils.get_icon_rect_and_handle_click(events, settings_icon_rect.left, settings_icon_rect.top,  settings_icon_rect.width, settings_icon_rect.height, const.STATE_SETTINGS)
        action_list.append(action)
        action = utils.handle_action_list(action_list, const.STATE_APARTMENT)
        action_list.clear()
        if action is not None:
            return action 

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
                        action = utils.use_inventory_item(product)
                        if action == "dead":
                            return const.STATE_START_SCREEN
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
                        elif apartment.debt_months_count > 3:
                            draw_functions.draw_message_box("You are in debt", f"You didn't pay rent for over 3 months and you are still in debt {apartment.debt} dollars")
                        else:
                            for i in const.real_estate_list:
                                if i.index != apartment.index:
                                    i.renting_apartment = False
                            draw_functions.draw_message_box("Welcome", "Welcome to your new apartment!")
                            apartment.renting_apartment = True
                            current_renting_apartment = apartment 
                            real_estate_card_surface = None
                            const.balance -= current_renting_apartment.get_monthly_renting_cost() - current_renting_apartment.rent_price
                            draw_apartment_list = False
                    if rect_list_apartment["buy"].collidepoint(mouse_pos):
                        draw_functions.draw_message_box("Button 2", "") #Buy
                    if "stop renting" in rect_list_apartment:
                        if rect_list_apartment["stop renting"].collidepoint(mouse_pos):
                            if apartment.index == 0:
                                draw_functions.draw_message_box("Tier 1", "Can't stop renting tier 1 apartment")
                            else:
                                draw_functions.draw_message_box(f"Tier {current_renting_apartment.index + 1}", f"You stopped renting tier {current_renting_apartment.index + 1} apartment and are back to tier 1")
                                apartment = tier_1_apartment
                                for i in const.real_estate_list:
                                    if i.index != apartment.index:
                                        i.renting_apartment = False
                                current_renting_apartment = tier_1_apartment
                                current_renting_apartment.renting_apartment = True
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
        
        if draw_apartment_list and not apartment.index == current_renting_apartment.index and real_estate_card_surface is None:
            real_estate_card_surface, rect_list_apartment, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, real_estate_buttons, apartment) 
            draw_inventory = False
            inventory_card_surface = None
            rect_list_inventory.clear()
        elif draw_apartment_list and apartment.index == current_renting_apartment.index and real_estate_card_surface is None:
            real_estate_card_surface, rect_list_apartment, x_coordinate, y_coordinate = draw_functions.create_card_surface(const.screen, const.job_button, const.job_cards_text, real_estate_buttons_when_renting, apartment) 
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

        utils.set_fps_clock(clock, 60)
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)