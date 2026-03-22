import pygame
import interface.city_screen as city_screen
import utils.draw_functions as draw_functions
import interface.apartment_screen as apartment_screen
import const 
import interface.casino_screen as casino_screen
import interface.job_interface.work_screen as work_screen
import interface.russian_roulette_screen as russian_roulette_screen
import interface.job_interface.janitor_screen as janitor_screen
import interface.job_interface.waiter_screen as waiter_screen
import interface.job_interface.slot_attendant_screen as slot_attendant_screen
import interface.job_interface.dealer_screen as dealer_screen
import interface.job_interface.shift_manager_screen as shift_manager_screen
import interface.job_interface.pit_boss_screen as pit_boss_screen
import interface.job_interface.shift_lead_screen as shift_lead_screen
import interface.job_interface.manager_screen as manager_screen
import interface.shopping_interface.shopping_center_screen as shopping_center_screen
import interface.shopping_interface.cars_section.cars_screen as cars_screen
import interface.shopping_interface.electronics_section.electronics_screen as electronics_screen
import interface.shopping_interface.furniture_section.furniture_screen as furniture_screen
import interface.shopping_interface.clothing_section.clothing_screen as clothing_screen
import interface.shopping_interface.tools_section.tools_screen as tools_screen
import interface.shopping_interface.groceries_section.groceries_screen as groceries_screen
import interface.shopping_interface.cars_section.sedan_car_section_screen as sedan_car_section_screen
import interface.shopping_interface.cars_section.sports_car_section_screen as sports_car_section_screen
import interface.shopping_interface.cars_section.pickup_car_section_screen as pickup_car_section_screen
import interface.shopping_interface.cars_section.hatchback_car_section_screen as hatchback_car_section_screen
import interface.shopping_interface.cars_section.suv_car_section_screen as suv_car_section_screen
import interface.shopping_interface.electronics_section.accessories_section_screen as accessories_section_screen
import interface.shopping_interface.electronics_section.consoles_section_screen as consoles_section_screen
import interface.shopping_interface.electronics_section.laptops_section_screen as laptops_section_screen
import interface.shopping_interface.electronics_section.smartphones_section_screen as smartphones_section_screen
import interface.shopping_interface.furniture_section.armchairs_section_screen as armchairs_section_screen
import interface.shopping_interface.furniture_section.tables_section_screen as tables_section_screen
import interface.shopping_interface.furniture_section.beds_section_screen as beds_section_screen
import interface.shopping_interface.furniture_section.bookshleves_section_screen as bookshleves_section_screen
import interface.shopping_interface.clothing_section.hoodie_section_screen as hoodie_section_screen
import interface.shopping_interface.clothing_section.pants_section_screen as pants_section_screen
import interface.shopping_interface.clothing_section.snees_section_screen as snees_section_screen
import interface.shopping_interface.clothing_section.tshirt_section_screen as tshirt_section_screen
import interface.shopping_interface.groceries_section.fruits_section_screen as fruits_section_screen
import interface.shopping_interface.groceries_section.bread_section_screen as bread_section_screen
import interface.shopping_interface.groceries_section.milk_section_screen as milk_section_screen
import interface.shopping_interface.groceries_section.vegetables_section_sceen as vegetables_section_screen
import interface.shopping_interface.tools_section.hand_tools_section_screen as hand_tools_section_screen
import interface.shopping_interface.tools_section.power_tools_section_screen as power_tools_section_screen
import interface.shopping_interface.tools_section.safety_gear_section_screen as safety_gear_section_screen
import interface.shopping_interface.tools_section.tools_accessories_section_screen as tools_accessories_section_screen
import interface.shopping_interface.electronics_section.accessories_section_screen as accessories_section_screen
import interface.shopping_interface.electronics_section.consoles_section_screen as consoles_section_screen
import interface.shopping_interface.electronics_section.laptops_section_screen as laptops_section_screen
import interface.shopping_interface.electronics_section.smartphones_section_screen as smartphones_section_screen
import interface.shopping_interface.furniture_section.armchairs_section_screen as armchairs_section_screen
import interface.shopping_interface.furniture_section.beds_section_screen as beds_section_screen
import interface.shopping_interface.furniture_section.bookshleves_section_screen as bookshleves_section_screen
import interface.shopping_interface.furniture_section.tables_section_screen as tables_section_screen
import utils.file_utils as file_utils
import sys
from tkinter import * 
from tkinter.ttk import *
import ast
import classes.items_class as items_class
import logic.inventory_items_logic as inventory_items_logic
import settings_screen as settings_screen

def grab_all_variables(file_path = "const.py", starts_with="STATE"):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.startswith(starts_with):
                        value = eval(ast.unparse(node.value))
                        key = target.id
                        const.screen_and_buy_functions.update({key:value})  
 
def get_icon_rect_and_handle_click(events, position_x, position_y, icon_width, icon_height, type):
    icon_rect = pygame.Rect(position_x, position_y,  icon_width, icon_height)
    for event in events:
        if event.type == pygame.QUIT:
            save_game()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_rect.collidepoint(event.pos):
            if type in const.screen_and_buy_functions.values():
                save_game()
                type()
                return
                
def buy(events, position_x, position_y, icon_width, icon_height, type, price, product):
    icon_rect = pygame.Rect(position_x, position_y,  icon_width, icon_height)
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_rect.collidepoint(event.pos):
            if type in const.screen_and_buy_functions.values():
                type(price, product)
                return

def process_bet_text_box_events(events, input_box, text, active):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                text = "Your bet: "
                active = True
                const.digit_counter = 0
                const.your_bet = 0
                const.bet = "" 
            else:
                active = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                if not text.endswith(' '):
                    if len(const.bet) > 0:
                        text = text[:-1]
                        const.digit_counter -= 1
                        const.bet = const.bet[:-1]
                        if const.bet:
                            const.your_bet = int(const.bet) 
                        else:
                            const.your_bet = 0
            else:
                if event.unicode in const.numbers and const.digit_counter < 7:
                    const.digit_counter += 1
                    const.bet += event.unicode 
                    text += event.unicode
                    const.your_bet = int(const.bet) 
                elif const.digit_counter >= 7:
                    draw_functions.draw_message_box('Wrong input', 'Nuber can not have more than 7 digits')
                else:
                    draw_functions.draw_message_box('Wrong input', 'You need to input numbers 0-9')
    return text, active

def handle_choice_buttons(events, button, boolChoice, counter, condition, rightButton):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button.collidepoint(mouse_pos):
            if mouse_click[0]:
                if  counter < condition and not boolChoice and rightButton:
                    counter += 1
                    boolChoice = True
                elif counter != condition and not boolChoice and not rightButton:
                    counter -= 1 
                    boolChoice = True
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                boolChoice = False
    return counter, boolChoice

def make_bet(choice, your_numbers, counter, counter2, counter3, counter4, counter5, counter6, choice_text = ""):
    your_numbers = []
    if choice == 1 or choice == 2:
        your_numbers.append(counter)
    elif choice == 3:
        your_numbers.append(-1)
    elif choice == 4:
        your_numbers.append(counter) 
        your_numbers.append(counter2)
    elif choice == 5:
        your_numbers.append(counter) 
        your_numbers.append(counter2)
        your_numbers.append(counter3)
    elif choice == 6:
        your_numbers.append(counter) 
        your_numbers.append(counter2)
        your_numbers.append(counter3)
        your_numbers.append(counter4)
    elif choice == 7:
        your_numbers.append(counter) 
        your_numbers.append(counter2)
        your_numbers.append(counter3)
        your_numbers.append(counter4)
        your_numbers.append(counter5) 
        your_numbers.append(counter6)
    elif choice == 8:
        your_numbers.append(0)
        your_numbers.append(counter2)
        your_numbers.append(counter3)
    elif choice == 9:
        if choice_text == "Odd nums":
            for i in range(0, 37):
                if(i%2!=0):
                    your_numbers.append(i)
        else:
            for i in range(0, 37):
                if(i%2==0):
                    your_numbers.append(i)
    elif choice == 10:
        if choice_text == "Low":
            for i in range(1, 19):
                your_numbers.append(i)
        if choice_text == "High":
            for i in range(19, 37):
                your_numbers.append(i)
    elif choice == 11:
        if choice_text == "Nums: 1-12":
            for i in range(1, 13):
                your_numbers.append(i)
        elif choice_text == "Nums: 13-24":
            for i in range(13, 25):
                your_numbers.append(i)
        else:
            for i in range(25, 37):
                your_numbers.append(i)
    return your_numbers
        
def date_time_timer():
    day_duration = 2000 # Day duration is 2 seconds
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [2, 4, 6, 9, 11]
    now = pygame.time.get_ticks()
    number_of_working_days_on_the_current_job = 3
    if now - const.date_time_ms >= day_duration:
        if const.working == 1:
            const.job_positions_list[const.index][number_of_working_days_on_the_current_job] += 1
        const.day_counter += 1
        const.return_day_counter += 1
        const.date_time_ms = now
    if const.year_counter % 4 == 0 or const.year_counter % 400 == 0:
        const.leap_year = True 
    if const.return_day_counter > 6:
        const.return_day_counter = 0
    elif const.day_counter > 28 and const.month_counter == 2 and not const.leap_year: #if its February and not leap year
        const.day_counter = 1
        const.month_counter += 1
        const.balance = round(const.balance + const.salary, 2)
        const.return_month_counter += 1
    elif const.day_counter > 29 and const.month_counter == 2 and const.leap_year: #if its February and it is leap year
        const.day_counter = 1
        const.month_counter += 1
        const.balance = round(const.balance + const.salary, 2)
        const.return_month_counter += 1
    elif const.day_counter > 31 and const.month_counter in days31:
        const.day_counter = 1
        const.month_counter += 1
        const.balance = round(const.balance + const.salary, 2)
        const.return_month_counter += 1
        if const.month_counter > 12 or const.return_month_counter > 11:
            const.month_counter = 1
            const.return_month_counter = 0
            const.year_counter += 1
    elif const.day_counter > 30 and const.month_counter in days30:
        const.day_counter = 1
        const.month_counter += 1
        const.balance = round(const.balance + const.salary, 2)
        const.return_month_counter += 1
    
    months = str(const.day_counter) + " of " + month[const.return_month_counter]
    return days[const.return_day_counter], months, const.year_counter

def job_details():
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    position_button = ""

    for button in const.buttons_list:
        button_rect = pygame.Rect(button[5][0], button[5][1], button[5][2], button[5][3])
        if button_rect.collidepoint(mouse_pos):
            position_button = button[2]
        if mouse_click[0] and position_button == "Janitor":
            janitor_screen.janitor_screen()
        if mouse_click[0] and position_button == "Waiter":
            waiter_screen.waiter_screen()
        if mouse_click[0] and position_button == "Slot Attendant":
            slot_attendant_screen.slot_attendant_screen()
        if mouse_click[0] and position_button == "Dealer":
            dealer_screen.dealer_screen()
        if mouse_click[0] and position_button == "Shift Manager":
            shift_manager_screen.shift_manager_screen()
        if mouse_click[0] and position_button == "Pit Boss":
            pit_boss_screen.pit_boss_screen()
        if mouse_click[0] and position_button == "Shift Lead":
            shift_lead_screen.shift_lead_screen()
        if mouse_click[0] and position_button == "Manager":
            manager_screen.manager_screen()

def job_apply(button_rect, salary, working_days_requirements, job):
    index = next((i for i, sublist in enumerate(const.job_positions_list) if sublist[0] == job), None)
    if index is None and not const.job_apply:
        draw_functions.draw_message_box('Application', "Job does not exist")
        const.job_apply = True
        return
    
    already_worked_on_this_position_indicator_index = 2
    janitor_job_index = 0
    currently_working_on_this_position_indicator_index = 4
    job_name_index = 0
    number_of_days_working_on_this_position_indicator_index = 3

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button_rect.collidepoint(mouse_pos):
        if mouse_click[0]:  
            if index == 0 and const.job_positions_list[janitor_job_index][already_worked_on_this_position_indicator_index] == False:
                const.index = index
                const.job_positions_list[janitor_job_index][already_worked_on_this_position_indicator_index] = True
                const.job_positions_list[janitor_job_index][number_of_days_working_on_this_position_indicator_index] = 0
                const.working = 1
                draw_functions.draw_message_box('Application', f"You have been accepted on the {job} position")
                const.salary = salary
                for job in const.job_positions_list: #reset all other currently working states on other jobs
                    job[currently_working_on_this_position_indicator_index] = False
                const.job_positions_list[janitor_job_index][currently_working_on_this_position_indicator_index] = True 
                return
            elif index == 0 and const.job_positions_list[janitor_job_index][already_worked_on_this_position_indicator_index] == True and const.job_positions_list[janitor_job_index][currently_working_on_this_position_indicator_index] == False:
                draw_functions.draw_message_box('Application', f"You are back at the {job} position")
                const.index = index
                const.salary = salary
                for job in const.job_positions_list:
                    job[currently_working_on_this_position_indicator_index] = False
                const.job_positions_list[janitor_job_index][currently_working_on_this_position_indicator_index] = True
                return

            prev_index = index - 1
            prev_done = const.job_positions_list[prev_index][already_worked_on_this_position_indicator_index]
            prev_days = const.job_positions_list[prev_index][number_of_days_working_on_this_position_indicator_index]

            if prev_done and prev_days >= working_days_requirements and const.job_positions_list[index][currently_working_on_this_position_indicator_index] == False:
                const.index = index
                const.job_positions_list[index][already_worked_on_this_position_indicator_index] = True  
                const.working = 1
                const.salary = salary
                draw_functions.draw_message_box('Application', f"You have been accepted on the {job} position")
                for job in const.job_positions_list:
                    job[currently_working_on_this_position_indicator_index] = False
                const.job_positions_list[index][currently_working_on_this_position_indicator_index] = True
                return
            elif const.job_positions_list[index][already_worked_on_this_position_indicator_index] == True and const.job_positions_list[index][currently_working_on_this_position_indicator_index] == False:
                draw_functions.draw_message_box('Application', f"You are back at the {job} position")
                const.index = index
                const.salary = salary
                for job in const.job_positions_list: 
                    job[currently_working_on_this_position_indicator_index] = False
                const.job_positions_list[index][currently_working_on_this_position_indicator_index] = True
                return
            
            if const.job_positions_list[index][currently_working_on_this_position_indicator_index] == True:
                draw_functions.draw_message_box('Application', f"You are already working as {job}")
                for job in const.job_positions_list: 
                    job[currently_working_on_this_position_indicator_index] = False
                const.job_positions_list[index][currently_working_on_this_position_indicator_index] = True
                return
            
            days_until_promotion = working_days_requirements - const.job_positions_list[prev_index][number_of_days_working_on_this_position_indicator_index]        
            draw_functions.draw_message_box('Application', f"Your application has been denied. You need {working_days_requirements} days on the {const.job_positions_list[prev_index][job_name_index]} position. {days_until_promotion} days remaining")

def restart_game():
    save_path = file_utils.extract_default_save()
    const.balance = 500
    const.salary = 0
    const.working = 0
    const.day_counter = 1
    const.month_counter = 1
    const.year_counter = 1990
    const.return_day_counter = 0
    const.return_month_counter = 0
    const.job_positions_list = [['janitor', 0, False, 0, False], ['waiter', 5, False, 0, False], ['slot attendant', 10, False, 0, False], ['dealer', 15, False, 0, False], ['shift leader', 20, False, 0, False], ['pit boss', 25, False, 0, False], ['shift manager', 30, False, 0, False], ['manager', 35, False, 0, False]]
    const.index = 0
    const.inventory_list_file = []
    const.inventory_list = []
    const.inventory_index = 0
    file_utils.update_value_in_file(save_path, "balance")
    file_utils.update_value_in_file(save_path, "salary")
    file_utils.update_value_in_file(save_path, "working")
    file_utils.update_value_in_file(save_path, "day_counter")
    file_utils.update_value_in_file(save_path, "month_counter")
    file_utils.update_value_in_file(save_path, "year_counter")
    file_utils.update_value_in_file(save_path, "return_day_counter")
    file_utils.update_value_in_file(save_path, "return_month_counter")
    file_utils.update_value_in_file(save_path, "index")
    file_utils.update_list_in_file(save_path, "job_positions_list", const.job_positions_list)
    file_utils.update_list_in_file(save_path, "inventory_list", const.inventory_list_file)
    import start_screen  
    start_screen.main_screen() 

def buy_product_and_add_to_the_inventory(price, product):
    if price > const.balance:
        draw_functions.draw_message_box("Work in progress", f"You don't have enough money! balance: {const.balance} price: {price}")
    else:
        const.balance = round(const.balance - price, 2)
        const.inventory_list.append(product)
        update_inventory_file()

def load_inventory_objects():
    inventory_items = []
    type = 0
    image_path = 1
    item_type = 2
    item_price = 3
    for item in const.inventory_list_file:
        inventory_item = items_class.shop_item(item[type], item[image_path], item[item_type], item[item_price])
        inventory_items.append(inventory_item)
    return inventory_items

def update_inventory_file():
    inventory = []
    const.inventory_list_file = []
    for item in const.inventory_list:
        inventory.append(item.type)
        inventory.append(item.image_path)
        inventory.append(item.item_type)
        inventory.append(item.item_price)
        const.inventory_list_file.append(inventory)
        inventory = []

def use_inventory_item(item):
    messages = {
        "car":  ("Used car", f"You went for a nice drive in your {item.item_type} car"),
        "clothes": ("Used clothes", f"You had nice time wearing your {item.item_type}"),
        "electronics": ("Used electronic device", f"You had nice time playing with your {item.item_type}"),
        "furniture": ("Used furniture", f"You had nice time using your {item.item_type}"),
        "groceries": ("Used groceries", f"You had nice time eating your {item.item_type}"),
        "tools": ("Used tools", f"You used your {item.item_type}")
    }
    if item.type in messages:
        title, text = messages[item.type]
        draw_functions.draw_message_box(title, text)
    if item.type == "groceries":
        remove_item_from_the_inventory(item)
    elif item.type != "groceries" and item.type != "car":
        breaking_chance = inventory_items_logic.chance_for_the_item_to_break()
        if breaking_chance is True:
            draw_functions.draw_message_box("Item broke", f"Your {item.item_type} broke down and no longer works")
            remove_item_from_the_inventory(item)
    elif item.type == "car":
        outcome = inventory_items_logic.car_break_crash_death(item)
        if outcome == "not repaired": 
           remove_item_from_the_inventory(item)
        if outcome == "dead":
            draw_functions.draw_message_box('You are dead', f"You died in a car crash, your balance is now 0 because you lost everything you had, and your game will restart")
            restart_game()

def remove_item_from_the_inventory(item):
    const.inventory_list.remove(item)
    update_inventory_file()
    if const.inventory_index > len(const.inventory_list) - 1:
        const.inventory_index = 0

def save_game():
    #Save/update date and time every time app closes or screen changes
    file_utils.update_value_in_file("save_files\\information.txt", "day_counter")        
    file_utils.update_value_in_file("save_files\\information.txt", "month_counter")
    file_utils.update_value_in_file("save_files\\information.txt", "year_counter")
    file_utils.update_value_in_file("save_files\\information.txt", "return_day_counter")
    file_utils.update_value_in_file("save_files\\information.txt", "return_month_counter")

    #Save/update balance every time app closes or screen changes
    file_utils.update_value_in_file("save_files\\information.txt", "balance")

    #Save/update inventory every time app closes or screen changes
    file_utils.update_list_in_file("save_files\\information.txt", "inventory_list", const.inventory_list_file)

    #Save/update job info
    file_utils.update_list_in_file("save_files\\information.txt", "job_positions_list", const.job_positions_list)
    file_utils.update_value_in_file("save_files\\information.txt", "index")
    file_utils.update_value_in_file("save_files\\information.txt", "salary")
    file_utils.update_value_in_file("save_files\\information.txt", "working")

def play_current_song():
    song = const.playlist[const.current_song_index]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(const.MUSIC_END)

def play_music(events):
    for event in events:
        if event.type == const.MUSIC_END:
            const.current_song_index = (const.current_song_index + 1) % len(const.playlist)
            play_current_song()