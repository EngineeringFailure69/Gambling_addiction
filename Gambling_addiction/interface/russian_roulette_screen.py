import pygame
import const
import utils.draw_functions as draw_functions
import utils.utils as utils
import logic.russian_roulette_logic as russian_roulette_logic
import utils.file_utils as file_utils
import sys
import text_messages

def russian_roulette_screen():
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)

    active = False
    drawn = False
    text = "Your bet: "
    prize = 0
    const.your_bet = 0
    bet = False
    barrell_spin = False
    you_play = False
    roll_player = 0
    roll_opponent = 0
    win = False 
    game_over = False

    spinning = False
    spin_start_ms = 0
    MESSAGE_DURATION_MS = 2000
  
    while running:
        events = pygame.event.get()
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\\game_russian_roulette_background.png")

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()

        if drawn == False:
            draw_functions.draw_message_box('Roulette info', text_messages.russian_roulette_text)
            drawn = True

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\\door_icon.webp", 75, 75, const.screen.get_width()-100, const.screen.get_height()-80)
        utils.get_icon_rect_and_handle_click(events, icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        text, active = utils.process_bet_text_box_events(events, const.your_bet_box, text, active)
        draw_functions.draw_text_box(const.screen, const.blue, const.your_bet_box, text, font, const.white)

        draw_functions.draw_button(const.screen, const.blue, const.bet_button, "Bet", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, const.pull_the_trigger_button, "Pull the trigger", font, const.black, mouse_pos)
        draw_functions.draw_button(const.screen, const.blue, const.spin_the_barrell_button, "Spin the barrell/roll the dice", font, const.black, mouse_pos)

        info_text = 'Balance:' + str(const.balance) + ' ' + 'Your bet: ' + str(const.your_bet) + " " + 'Prize: ' + str(prize)
        if const.bet_button.collidepoint(mouse_pos):
            if mouse_click[0] and not barrell_spin:
                if const.your_bet <= 0:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars")
                    bet = False
                elif const.your_bet < const.balance * 0.20 and const.balance <= 9999999:
                    draw_functions.draw_message_box('Bet error', f"You  have to bet at least {int(const.balance * 0.20)+1} dollars, which is 20% of your total balance")
                    bet = False
                elif const.balance < const.your_bet:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, because your current balance is {const.balance}")
                    bet = False
                else:
                    prize = russian_roulette_logic.to_win(const.your_bet)
                    bet = True
        
        if const.spin_the_barrell_button.collidepoint(mouse_pos):
            if mouse_click[0] and bet == True and not barrell_spin:
                russian_roulette_logic.spin_the_barrell()
                you_play, roll_player, roll_opponent = russian_roulette_logic.roll_the_dice(you_play)
                barrell_spin = True
                spinning = True
                spin_start_ms = now
            elif mouse_click[0] and not bet:
                draw_functions.draw_message_box('Bet error', "You need to place a bet first")
                barrell_spin = False
            elif mouse_click[0] and barrell_spin:
                draw_functions.draw_message_box('Spin error', "Barrell spin has already been done, you can't spin barrell more than once")

        if spinning:
            draw_functions.draw_custom_message_box(const.screen, text_messages.barrel_text, font)
    
            # check if the spinning is over
            if now - spin_start_ms >= MESSAGE_DURATION_MS:
                draw_functions.draw_message_box('Dice result', f"{text_messages.dice_text}\nPlayer roll: {roll_player}\nOpponent roll: {roll_opponent}\n You play first: {str(you_play)}")
                spinning = False

        if const.pull_the_trigger_button.collidepoint(mouse_pos):
            if mouse_click[0] and bet == True and barrell_spin == True:
                win, game_over, you_play = russian_roulette_logic.pull_the_trigger(you_play)
                if win and game_over:
                    const.balance += prize
                    draw_functions.draw_message_box('You won', f"You won the game, prize is {str(prize)}, your current balance is {str(const.balance)}")
                    file_utils.update_value_in_file("save_files\\information.txt", "balance")
                    barrell_spin = False
                if not win and game_over:
                    draw_functions.draw_message_box('You lost', f"You lost the game, you are dead, your balance is now 0 because you lost everything you had, and your game will restart")
                    utils.restart_game()
                    return
                elif not win and not game_over and you_play:
                    draw_functions.draw_message_box('Round over', "Your opponent survived, you play now")
                elif not win and not game_over and not you_play:
                    draw_functions.draw_message_box('Round over', "You survived, your opponent plays now")
            elif mouse_click[0] and not bet and barrell_spin == True:
                draw_functions.draw_message_box('Bet error', "You need to place a bet first")
            elif mouse_click[0] and bet == True and not barrell_spin:
                draw_functions.draw_message_box('Spin error', "You need to spin the barrell first")
            elif mouse_click[0] and not bet and not barrell_spin:
                draw_functions.draw_message_box('Roulette error', "You need to place the bet and spin the barrell first")

        draw_functions.draw_button(const.screen, const.table_brown, const.info, info_text, font, const.white)
    
        pygame.display.flip()
    pygame.quit()
    sys.exit(0)