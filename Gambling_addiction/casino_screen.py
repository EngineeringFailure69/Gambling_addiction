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
    right_choice11_clicked_up = False
    left_choice11_clicked_up = False

    # Definiši textbox
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
    text = "Your bet: "
    selected_colour = "Red"
    choice9_text = "Even num"
    choice10_text = "Low (1-18)"
    choice11_text = "Nums: 1-12"
    choice11_counter = 1
    choice = 1

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
            
        if right_choice_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                if  choice<11 and not right_choice_clicked_up:
                    choice += 1
                    right_choice_clicked_up = True
            
        if left_choice_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                if choice > 1 and not left_choice_clicked_up:
                    choice -= 1
                    left_choice_clicked_up = True

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    right_choice_clicked_up = False
                    left_choice_clicked_up = False
                    right_choice11_clicked_up = False
                    left_choice11_clicked_up = False

        # end of functionalities elements drawings

        if bet_button.collidepoint(mouse_pos):
            if mouse_click[0]:
                return

        info = pygame.Rect(const.screen.get_width()-const.button_width-900, const.screen.get_height()-const.button_height+30, const.button_width+800, const.button_height-30)
        draw_functions.draw_button(const.screen, const.green, info, 'balance:' + str(const.balance), font, const.black)

        # Draw choices

        if choice == 1 or choice == 2:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
        elif choice == 3:
            print("Something, will make it later")
        elif choice == 4:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)
        elif choice == 5:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
        elif choice == 6:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            
            draw_functions.draw_button(const.screen, const.blue, choice4_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice4_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice4_button, "<-", font, const.black)
        elif choice == 7:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
            
            draw_functions.draw_button(const.screen, const.blue, choice4_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice4_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice4_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice5_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice5_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice5_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice6_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice6_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice6_button, "<-", font, const.black)
        elif choice == 8:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, "Number: 0", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice2_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice2_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice2_button, "<-", font, const.black)

            draw_functions.draw_button(const.screen, const.blue, choice3_button, "Number: ", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice3_button, "->", font, const.black)
            draw_functions.draw_button(const.screen, const.blue, left_choice3_button, "<-", font, const.black)
        elif choice == 9:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice9_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Even num"
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice9_text = "Odd num"
        elif choice == 10:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice10_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "Low (1-18)"
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0]:
                    choice10_text = "High (19-36)"
        elif choice == 11:
            draw_functions.draw_button(const.screen, const.blue, choice1_button, choice11_text, font, const.black)
            draw_functions.draw_button(const.screen, const.blue, right_choice1_button, "->", font, const.black)
            if right_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0] and not right_choice11_clicked_up:
                    choice11_counter += 1  
                    right_choice11_clicked_up = True
            draw_functions.draw_button(const.screen, const.blue, left_choice1_button, "<-", font, const.black)
            if left_choice1_button.collidepoint(mouse_pos):
                if mouse_click[0] and not left_choice11_clicked_up:
                    choice11_counter -= 1
                    left_choice11_clicked_up = True
            
            if choice11_counter == 1:
                choice11_text = "Nums: 1-12"
            elif choice11_counter == 2:
                choice11_text = "Nums: 13-24"
            elif choice11_counter == 3:
                choice11_text = "Nums: 25-36"
        # end of draw choices

        pygame.display.flip()
    pygame.quit()
    exit()