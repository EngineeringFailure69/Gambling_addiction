import pygame
import const
import draw_functions
import utils
import sys

def casino_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    drawn = False
    right_choice_clicked_up = False
    left_choice_clicked_up = False

    # Definiši textbox
    bet_button = pygame.Rect(const.screen.get_width()//60, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    your_bet = pygame.Rect(const.screen.get_width()-1100, const.screen.get_height()//50, const.button_width, const.button_height-50)
    pick_colour_button = pygame.Rect(const.screen.get_width()-710, const.screen.get_height()//50, const.button_width-200, const.button_height-50)
    red_colour_button = pygame.Rect(const.screen.get_width()-600, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    black_colour_button = pygame.Rect(const.screen.get_width()-770, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    choice_Info_button = pygame.Rect(const.screen.get_width()-180, const.screen.get_height()//50, const.button_width-150, const.button_height-50)

    right_choice_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    left_choice_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    colour_choice_Info_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//50, const.button_width-150, const.button_height-50)

    active = False
    text = "Your bet: "
    selected_colour = "Red"
    choice_text = "Chouse: "
    choice = 0

    while running:

        events = pygame.event.get()
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\casino_roulette.jpg")

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, 1120, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_EXIT_APARTMENT)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if drawn == False:
            draw_functions.draw_message_box('Gambling info', const.casino_screen_message_box)
            drawn = True

        # Casino functionalities elements drawings
        
        draw_functions.draw_button(const.screen, const.blue, bet_button, "Bet", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, choice_Info_button, "Choice Info", font, const.black)
        if choice_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                draw_functions.draw_message_box('Choice info', const.choice_info_text)

        text, active = utils.process_bet_text_box_events(events, your_bet, text, active)
        draw_functions.draw_text_box(const.screen, const.blue, your_bet, text, font, const.black)

        draw_functions.draw_button(const.screen, const.blue, pick_colour_button, selected_colour, font, const.black)

        draw_functions.draw_button(const.screen, const.blue, red_colour_button, "->", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, black_colour_button, "<-", font, const.black)

        draw_functions.draw_button(const.screen, const.blue, colour_choice_Info_button, "Choice: " + str(choice), font, const.black)

        draw_functions.draw_button(const.screen, const.blue, right_choice_button, "->", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, left_choice_button, "<-", font, const.black)
        
        if red_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Red"
            
        if black_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Black"
            
        if right_choice_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                if  choice<12 and not right_choice_clicked_up:
                    choice += 1
                    right_choice_clicked_up = True
            
        if left_choice_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                if choice > 0 and not left_choice_clicked_up:
                    choice -= 1
                    left_choice_clicked_up = True

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    right_choice_clicked_up = False
                    left_choice_clicked_up = False

        # end of functionalities elements drawings

        if bet_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                return

        info = pygame.Rect(const.screen.get_width()-const.button_width-900, const.screen.get_height()-const.button_height+30, const.button_width+800, const.button_height-30)
        draw_functions.draw_button(const.screen, const.green, info, 'balance:' + str(const.balance), font, const.black)

        pygame.display.flip()
    pygame.quit()
    exit()