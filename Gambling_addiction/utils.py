import pygame
import city_screen
import draw_functions
import apartment_screen
import const
import casino_screen
import work_screen
import sys

def get_icon_rect_and_handle_click(position_x, position_y, icon_width, icon_height, type):
    icon_rect = pygame.Rect(position_x, position_y,  icon_width, icon_height)
    handle_icon_click(icon_rect, type)

def handle_icon_click(icon_rect, type):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if icon_rect.collidepoint(mouse_pos) and type == "casino":
        if(mouse_click[0]):
            casino_screen.casino_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "apartment":
        if(mouse_click[0]):
            apartment_screen.apartment_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "exit_door":
        if(mouse_click[0]):
            city_screen.city_screen()
    if icon_rect.collidepoint(mouse_pos) and type == "work":
        if(mouse_click[0]):
            work_screen.work_screen()

def handle_quit(running):
    for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
    return running

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
            else:
                active = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                if const.bet != "":
                    formatted_bet = draw_functions.format_number(const.bet)
                    text = "Your bet: " + formatted_bet  # dodaj formatirani broj u tekst
                    const.bet = ""         # resetuj unos
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
                const.digit_counter -= 1
            else:
                if event.unicode in const.numbers and const.digit_counter < 7:
                    const.digit_counter += 1
                    const.bet += event.unicode 
                    text += event.unicode 
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

def handle_mouse_button_up_event(events, boolChoice):
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                boolChoice = False
    return boolChoice