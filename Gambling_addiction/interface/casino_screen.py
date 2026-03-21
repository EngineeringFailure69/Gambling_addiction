import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import logic.casino_roulette_logic as casino_roulette_logic
import sys
import text_messages

def casino_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    img_path = "background_photos\\start_screen_background.png"
    drawn = False
    win_lose_drawn = False
    right_choice_clicked_up = False
    left_choice_clicked_up = False
    right_choice1_clicked_up = False
    left_choice1_clicked_up = False
    won = False
    const.your_bet = 0

    active = False
    return_colour = "" 
    info_text = ""
    choice_text = ""
    text = "Your bet: "
    your_numbers = []
    selected_colour = "Black"
    choice9_text = "Even nums"
    choice10_text = "Low (1-18)"
    choice11_text = "Nums: 1-12"
    spinning = True
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

    spinning = False
    done_spinning = False
    spin_start_ms = 0
    MESSAGE_DURATION_MS = 5000
    MESSAGE_GAP = 500
    spin_end_ms = 0

    icon_center_x = 450
    icon_center_y = 290
    icon_path = "icons\\start_screen_roulette_wheel.png"
    icon_width_animation = 700
    icon_height_animation = 470
    angle = 0
    rotated_rect = 0
    angle_increment = 0
    COUNTER_CLOCK_WISE = True

    draw_functions.load_background_image(const.screen, img_path)
    
    clock = pygame.time.Clock()
    while running:
        events = pygame.event.get()
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, img_path)
        angle, rotated_rect = draw_functions.load_spin_animation(const.screen, icon_center_x, icon_center_y, angle, icon_path, icon_width_animation, icon_height_animation, rotated_rect, angle_increment, COUNTER_CLOCK_WISE)

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, const.door_icon_path, const.door_icon_width, const.door_icon_height, const.door_icon_position_x, const.door_icon_position_y)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()

        if drawn == False:
            draw_functions.draw_message_box('Gambling info', text_messages.casino_screen_message_box)
            drawn = True

        # Casino functionalities elements drawings

        draw_functions.draw_button(const.screen, const.blue, const.bet_button, "Bet", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, const.choice_Info_button, "Choice Info", font, const.black, mouse_pos)
        if const.choice_Info_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                draw_functions.draw_message_box('Choice info', text_messages.choice_info_text)

        text, active = utils.process_bet_text_box_events(events, const.your_bet_box, text, active)
        draw_functions.draw_text_box(const.screen, const.blue, const.your_bet_box, text, font, const.white)

        draw_functions.draw_button(const.screen, const.blue, const.pick_colour_button, selected_colour, font, const.black)

        draw_functions.draw_button(const.screen, const.blue, const.red_colour_button, "->", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, const.black_colour_button, "<-", font, const.black, mouse_pos)

        draw_functions.draw_button(const.screen, const.blue, const.choice_button, "Choice: " + str(choice), font, const.black)

        draw_functions.draw_button(const.screen, const.blue, const.right_choice_button, "->", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, const.left_choice_button, "<-", font, const.black, mouse_pos)

        if const.red_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Red"
            
        if const.black_colour_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                selected_colour = "Black"

        choice, right_choice_clicked_up = utils.handle_choice_buttons(events, const.right_choice_button, right_choice_clicked_up, choice, 11, True)
        choice, left_choice_clicked_up = utils.handle_choice_buttons(events, const.left_choice_button, left_choice_clicked_up, choice, 1, False)

        # end of functionalities elements drawings

        info_text = 'Balance:' + str(const.balance) + ' ' + 'Your bet: ' + str(const.your_bet) + ' ' + 'Table: ' + str(table) + " " + 'Prize: ' + str(prize)
        if const.bet_button.collidepoint(mouse_pos):
            if mouse_click[0] and not spinning:
                if const.balance < const.your_bet:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, because your current balance is {const.balance}")
                elif const.your_bet <= 0:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars")
                elif choice == 3 and const.your_bet > const.balance * 0.1 + 1:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, for this choice you can only bet up to 10% of your budget, which is {int(const.balance * 0.1)+1}")
                elif choice == 9 and const.your_bet > const.balance * 0.1 + 1:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, for this choice you can only bet up to 10% of your budget, which is {int(const.balance * 0.1)+1}")
                elif choice == 10 and const.your_bet > const.balance * 0.1 + 1:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, for this choice you can only bet up to 10% of your budget, which is {int(const.balance * 0.1)+1}")
                elif choice == 11 and const.your_bet > const.balance * 0.2 + 1:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, for this choice you can only bet up to 20% of your budget, which is {int(const.balance * 0.2)+1}")
                else:    
                    prize, table, return_colour = casino_roulette_logic.to_win_function(choice, const.your_bet, selected_colour, your_numbers)
                    spinning = True
                    spin_start_ms = now
                    win_lose_drawn = False
                
        if spinning:
            #start spinning animation
            angle_increment = 2
            angle, rotated_rect = draw_functions.load_spin_animation(const.screen, icon_center_x, icon_center_y, angle, icon_path, icon_width_animation, icon_height_animation, rotated_rect, angle_increment, COUNTER_CLOCK_WISE)
            # draw custom box
            draw_functions.draw_custom_message_box(const.screen, "Spinning the wheel...", font)
            # check if the spinning is over
            if now - spin_start_ms >= MESSAGE_DURATION_MS:
                angle_increment = 0
                spinning = False
                done_spinning = True
                spin_end_ms = now
                your_numbers = utils.make_bet(choice, your_numbers, counter, counter2, counter3, counter4, counter5, counter6, choice_text)
                const.balance, prize, table, won, return_colour, spin, spin_colour = casino_roulette_logic.casino_roulette(const.balance, const.your_bet, choice, selected_colour, your_numbers)


        if done_spinning:
            if now-spin_end_ms >= MESSAGE_GAP: 
                spinning = False
                if won == True and not win_lose_drawn:
                    draw_functions.draw_message_box('You won', f"Your numbers were: {str(your_numbers)}\n Your colour was: {return_colour}\n It landed on number: {str(spin)}\n It landed on colour: {spin_colour}\n You won {prize} dollars\n Your balance now is: {const.balance}")
                    win_lose_drawn = True
                    table = 0
                    prize = 0
                    text = "Your bet: "
                    const.your_bet = 0
                elif won == False and not win_lose_drawn:
                    draw_functions.draw_message_box('You lost', f"Your numbers were: {str(your_numbers)}\n Your colour was: {return_colour}\n It landed on number: {str(spin)}\n It landed on colour: {spin_colour}\n You lost {const.your_bet} dollars\n Your balance now is: {const.balance}")
                    table = 0
                    prize = 0
                    text = "Your bet: "
                    const.your_bet = 0
                    win_lose_drawn = True
                done_spinning = False

        if choice != prev_choice:
            counter = 0
            counter2  = 0
            counter3  = 0
            counter4  = 0
            counter5  = 0
            counter6  = 0
            prev_choice = choice
            
        draw_functions.draw_button(const.screen, const.green, const.info, info_text, font, const.black)

        # Draw choices

        if choice == 1:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)
        elif choice == 2:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)
        elif choice == 4:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, const.choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice2_button, "->", font, const.black, mouse_pos)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice2_button, "<-", font, const.black, mouse_pos)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice2_button, left_choice1_clicked_up, counter2, 0, False)
        elif choice == 5:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice2_button, "->", font, const.black, mouse_pos)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice2_button, "<-", font, const.black, mouse_pos)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice3_button, "->", font, const.black, mouse_pos)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice3_button, "<-", font, const.black, mouse_pos)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
        elif choice == 6:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice2_button, "->", font, const.black, mouse_pos)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice2_button, "<-", font, const.black, mouse_pos)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice3_button, "->", font, const.black, mouse_pos)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice3_button, "<-", font, const.black, mouse_pos)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, const.choice4_button, "Number: " + str(counter4), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice4_button, "->", font, const.black, mouse_pos)
            counter4, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice4_button, right_choice1_clicked_up, counter4, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice4_button, "<-", font, const.black, mouse_pos)
            counter4, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice4_button, left_choice1_clicked_up, counter4, 0, False)
        elif choice == 7:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: " + str(counter), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            counter, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice1_button, right_choice1_clicked_up, counter, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            counter, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice1_button, left_choice1_clicked_up, counter, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice2_button, "->", font, const.black, mouse_pos)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice2_button, "<-", font, const.black, mouse_pos)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice3_button, "->", font, const.black, mouse_pos)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice3_button, "<-", font, const.black, mouse_pos)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
            
            draw_functions.draw_button(const.screen, const.blue, const.choice4_button, "Number: " + str(counter4), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice4_button, "->", font, const.black, mouse_pos)
            counter4, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice4_button, right_choice1_clicked_up, counter4, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice4_button, "<-", font, const.black, mouse_pos)
            counter4, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice4_button, left_choice1_clicked_up, counter4, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice5_button, "Number: " + str(counter5), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice5_button, "->", font, const.black, mouse_pos)
            counter5, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice5_button, right_choice1_clicked_up, counter5, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice5_button, "<-", font, const.black, mouse_pos)
            counter5, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice5_button, left_choice1_clicked_up, counter5, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice6_button, "Number: " + str(counter6), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice6_button, "->", font, const.black, mouse_pos)
            counter6, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice6_button, right_choice1_clicked_up, counter6, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice6_button, "<-", font, const.black, mouse_pos)
            counter6, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice6_button, left_choice1_clicked_up, counter6, 0, False)
        elif choice == 8:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, "Number: 0", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, const.choice2_button, "Number: " + str(counter2), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice2_button, "->", font, const.black, mouse_pos)
            counter2, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice2_button, right_choice1_clicked_up, counter2, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice2_button, "<-", font, const.black, mouse_pos)
            counter2, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice2_button, left_choice1_clicked_up, counter2, 0, False)

            draw_functions.draw_button(const.screen, const.blue, const.choice3_button, "Number: " + str(counter3), font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice3_button, "->", font, const.black, mouse_pos)
            counter3, right_choice1_clicked_up = utils.handle_choice_buttons(events, const.right_choice3_button, right_choice1_clicked_up, counter3, 36, True)
            draw_functions.draw_button(const.screen, const.blue, const.left_choice3_button, "<-", font, const.black, mouse_pos)
            counter3, left_choice1_clicked_up = utils.handle_choice_buttons(events, const.left_choice3_button, left_choice1_clicked_up, counter3, 0, False)
        elif choice == 9:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, choice9_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            if const.right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Odd nums"
                    choice_text = choice9_text
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            if const.left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Even nums"
                    choice_text = choice9_text
        elif choice == 10:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, choice10_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            if const.right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "High (19-36)"
                    choice_text = "High"
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            if const.left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "Low (1-18)"
                    choice_text = "Low"
        elif choice == 11:
            draw_functions.draw_button(const.screen, const.blue, const.choice1_button, choice11_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, const.right_choice1_button, "->", font, const.black, mouse_pos)
            right_choice1_clicked_up = utils.handle_mouse_button_up_event(events, right_choice1_clicked_up)
            left_choice1_clicked_up = utils.handle_mouse_button_up_event(events, left_choice1_clicked_up)
            if const.right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0] and not right_choice1_clicked_up:
                    choice11_counter += 1  
                    right_choice1_clicked_up = True
            draw_functions.draw_button(const.screen, const.blue, const.left_choice1_button, "<-", font, const.black, mouse_pos)
            if const.left_choice1_button.collidepoint(mouse_pos):
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

        if const.fps_show:
            draw_functions.show_fps_counter(const.screen, clock, const.black, pygame.Rect(10, 570, 130, 20), font, 60, 5)

        pygame.display.flip()
    pygame.quit()
    sys.exit(0)