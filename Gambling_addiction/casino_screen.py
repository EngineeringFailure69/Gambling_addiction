import pygame
import const
import draw_functions
import utils
import sys
import casino_roulette_logic

def casino_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    drawn = False
    right_choice_clicked_up = False
    left_choice_clicked_up = False
    right_choice1_clicked_up = False
    left_choice1_clicked_up = False
    won = False

    # Define textbox
    bet_button = pygame.Rect(const.screen.get_width()//60, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    your_bet = pygame.Rect(const.screen.get_width()-1100, const.screen.get_height()//50, const.button_width, const.button_height-50)
    pick_colour_button = pygame.Rect(const.screen.get_width()-710, const.screen.get_height()//50, const.button_width-200, const.button_height-50)
    red_colour_button = pygame.Rect(const.screen.get_width()-600, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    black_colour_button = pygame.Rect(const.screen.get_width()-770, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    choice_Info_button = pygame.Rect(const.screen.get_width()-180, const.screen.get_height()//50, const.button_width-150, const.button_height-50)
    right_choice_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    left_choice_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    choice_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//50, const.button_width-150, const.button_height-50)

    right_choice1_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//10, const.button_width-250, const.button_height-50)
    left_choice1_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//10, const.button_width-250, const.button_height-50)
    choice1_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//10, const.button_width-150, const.button_height-50)
    
    right_choice2_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//5.5, const.button_width-250, const.button_height-50)
    left_choice2_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//5.5, const.button_width-250, const.button_height-50)
    choice2_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//5.5, const.button_width-150, const.button_height-50)

    right_choice3_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//3.8, const.button_width-250, const.button_height-50)
    left_choice3_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//3.8, const.button_width-250, const.button_height-50)
    choice3_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//3.8, const.button_width-150, const.button_height-50)

    right_choice4_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//2.9, const.button_width-250, const.button_height-50)
    left_choice4_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//2.9, const.button_width-250, const.button_height-50)
    choice4_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//2.9, const.button_width-150, const.button_height-50)

    right_choice5_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//2.35, const.button_width-250, const.button_height-50)
    left_choice5_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//2.35, const.button_width-250, const.button_height-50)
    choice5_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//2.35, const.button_width-150, const.button_height-50)

    right_choice6_button = pygame.Rect(const.screen.get_width()-300, const.screen.get_height()//2, const.button_width-250, const.button_height-50)
    left_choice6_button = pygame.Rect(const.screen.get_width()-520, const.screen.get_height()//2, const.button_width-250, const.button_height-50)
    choice6_button = pygame.Rect(const.screen.get_width()-460, const.screen.get_height()//2, const.button_width-150, const.button_height-50)

    active = False
    return_colour = "" 
    info_text = ""
    choice_text = ""
    text = "Your bet: "
    your_numbers = []
    selected_colour = "Black"
    choice9_text = "Even num"
    choice10_text = "Low (1-18)"
    choice11_text = "Nums: 1-12"
    spin = 0
    spin_colour = ""
    choice11_counter = 1
    choice = 1 
    prev_choice = choice
    counter = 0
    counter2  = 0
    counter3  = 0
    counter4  = 0
    counter5  = 0
    counter6  = 0
    prize = 0
    table = 0

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

        draw_functions.draw_button(const.screen, const.blue, choice_button, "Choice: " + str(choice), font, const.black)

        draw_functions.draw_button(const.screen, const.blue, right_choice_button, "->", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, left_choice_button, "<-", font, const.black)
        
        if red_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Red"
            
        if black_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Black"

        choice, right_choice_clicked_up = utils.handle_choice_buttons(events, right_choice_button, right_choice_clicked_up, choice, 11, True)
        choice, left_choice_clicked_up = utils.handle_choice_buttons(events, left_choice_button, left_choice_clicked_up, choice, 1, False)

        # end of functionalities elements drawings

        info_text = 'balance:' + str(const.balance) + ' ' + 'your bet: ' + str(const.your_bet) + ' ' + 'Table: ' + str(table) + " " + 'Prize: ' + str(prize)
        if bet_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                your_numbers = utils.make_bet(choice, your_numbers, counter, counter2, counter3, counter4, counter5, counter6, choice_text)
                if const.balance < const.your_bet:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, because your current balance is {const.balance}")
                else:
                    const.balance, prize, table, won, return_colour, spin, spin_colour = casino_roulette_logic.casino_roulette(const.balance, const.your_bet, choice, selected_colour, your_numbers)
                    if won == True:
                        draw_functions.draw_message_box('You won', f"Your numbers were: {str(your_numbers)}\n Your colour was: {return_colour}\n It landed on number: {str(spin)}\n It landed on colour: {spin_colour}\n You won {prize} dollars\n Your balance now is: {const.balance}")
                    else:
                        draw_functions.draw_message_box('You lost', f"Your numbers were: {str(your_numbers)}\n Your colour was: {return_colour}\n It landed on number: {str(spin)}\n It landed on colour: {spin_colour}\n You lost {const.your_bet} dollars\n Your balance now is: {const.balance}, ")
 
        if choice != prev_choice:
            counter = 0
            counter2  = 0
            counter3  = 0
            counter4  = 0
            counter5  = 0
            counter6  = 0
            prev_choice = choice

        info = pygame.Rect(const.screen.get_width()-const.button_width-900, const.screen.get_height()-const.button_height+30, const.button_width+800, const.button_height-30)
        draw_functions.draw_button(const.screen, const.green, info, info_text, font, const.black)

        # Draw choices

        if choice == 1:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)
        elif choice == 2:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)
        # elif choice == 3:
        #     print("Something, will make it later")
        elif choice == 4:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice2_button, left_choice1_clicked_up, counter2, 0, False)
        elif choice == 5:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
        elif choice == 6:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, choice4_button, "Number: " + str(counter4), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice4_button, "->", font, const.black)
            counter4, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice4_button, right_choice1_clicked_up, counter4, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice4_button, "<-", font, const.black)
            counter4, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice4_button, left_choice1_clicked_up, counter4, 0, False)
        elif choice == 7:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, choice4_button, "Number: " + str(counter4), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice4_button, "->", font, const.black)
            counter4, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice4_button, right_choice1_clicked_up, counter4, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice4_button, "<-", font, const.black)
            counter4, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice4_button, left_choice1_clicked_up, counter4, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice5_button, "Number: " + str(counter5), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice5_button, "->", font, const.black)
            counter5, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice5_button, right_choice1_clicked_up, counter5, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice5_button, "<-", font, const.black)
            counter5, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice5_button, left_choice1_clicked_up, counter5, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice6_button, "Number: " + str(counter6), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice6_button, "->", font, const.black)
            counter6, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice6_button, right_choice1_clicked_up, counter6, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice6_button, "<-", font, const.black)
            counter6, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice6_button, left_choice1_clicked_up, counter6, 0, False)
        elif choice == 8:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: 0", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
        elif choice == 9:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice9_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Odd nums"
                    choice_text = choice9_text
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Even nums"
                    choice_text = choice9_text
        elif choice == 10:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice10_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "High (19-36)"
                    choice_text = choice10_text
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "Low (1-18)"
                    choice_text = choice10_text
        elif choice == 11:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice11_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            right_choice1_clicked_up = utils.handle_mouse_button_up_event(events, right_choice1_clicked_up)
            left_choice1_clicked_up = utils.handle_mouse_button_up_event(events, left_choice1_clicked_up)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0] and not right_choice1_clicked_up:
                    choice11_counter += 1  
                    right_choice1_clicked_up = True
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0] and not left_choice1_clicked_up:
                    choice11_counter -= 1
                    left_choice1_clicked_up = True
            
            if choice11_counter == 1:
                choice11_text = "Nums: 1-12"
            elif choice11_counter == 2:
                choice11_text = "Nums: 13-24"
            elif choice11_counter == 3:
                choice11_text = "Nums: 25-36"
            choice_text = choice11_text
        # end of draw choices

        pygame.display.flip()
    pygame.quit()
    exit()