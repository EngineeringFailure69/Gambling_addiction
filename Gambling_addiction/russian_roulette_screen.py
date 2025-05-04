import pygame
import const
import draw_functions
import utils
import russian_roulette_logic

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

    spinning = False
    spin_start_ms = 0
    MESSAGE_DURATION_MS = 2000

    your_bet = pygame.Rect(const.screen.get_width()-1100, const.screen.get_height()//50, const.button_width, const.button_height-50)
    bet_button = pygame.Rect(const.screen.get_width()//60, const.screen.get_height()//50, const.button_width-250, const.button_height-50)
    pull_the_trigger_button = pygame.Rect(const.screen.get_width()-180, const.screen.get_height()//50, const.button_width-150, const.button_height-50)
    spin_the_barrell_button = pygame.Rect(const.screen.get_width()-375, const.screen.get_height()//50, const.button_width-140, const.button_height-50)

    while running:

        events = pygame.event.get()
        const.screen.fill(const.white)
        draw_functions.load_background_image(const.screen, "background_photos\game_russian_roulette_background.png")

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()

        if drawn == False:
            draw_functions.draw_message_box('Roulette info', const.russian_roulette_text)
            drawn = True

        icon_position_x, icon_position_y,  icon_width, icon_height = draw_functions.load_icons(const.screen, "icons\door_icon.webp", 75, 75, 1100, 520)
        utils.get_icon_rect_and_handle_click(icon_position_x, icon_position_y,  icon_width, icon_height, const.STATE_TO_THE_STREETS)

        text, active = utils.process_bet_text_box_events(events, your_bet, text, active)
        draw_functions.draw_text_box(const.screen, const.blue, your_bet, text, font, const.white)

        draw_functions.draw_button(const.screen, const.blue, bet_button, "Bet", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, pull_the_trigger_button, "Pull the trigger", font, const.black)
        draw_functions.draw_button(const.screen, const.blue, spin_the_barrell_button, "Spin the barrell", font, const.black)

        info_text = 'Balance:' + str(const.balance) + ' ' + 'Your bet: ' + str(const.your_bet) + " " + 'Prize: ' + str(prize)
        if bet_button.collidepoint(mouse_pos):
            if mouse_click[0] and not barrell_spin:
                if const.balance < const.your_bet:
                    draw_functions.draw_message_box('Bet error', f"You can not bet {const.your_bet} dollars, because your current balance is {const.balance}")
                    bet = False
                else:
                    prize = russian_roulette_logic.to_win(const.your_bet)
                    bet = True
        
        if spin_the_barrell_button.collidepoint(mouse_pos):
            if mouse_click[0] and bet == True and not barrell_spin:
                russian_roulette_logic.spin_the_barrell()
                #draw_functions.draw_message_box('Spin result', f"Bullet chamber: {const.bullet_chamber}\nCurrent chamber: {const.current_chamber}")
                barrell_spin = True
                spinning = True
                spin_start_ms = now
            elif mouse_click[0] and not bet:
                draw_functions.draw_message_box('Bet error', "You need to place a bet first")
                barrell_spin = False
            elif mouse_click[0] and barrell_spin:
                draw_functions.draw_message_box('Spin error', "Barrell spin has already been done, you can't spin barrell more than once")

        if spinning:
            draw_functions.draw_custom_message_box(const.screen, "Spinning the barrell...", font)
    
            # check if the spinning is over
            if now - spin_start_ms >= MESSAGE_DURATION_MS:
                spinning = False

        if pull_the_trigger_button.collidepoint(mouse_pos):
            if mouse_click[0] and bet == True and barrell_spin == True:
                draw_functions.draw_message_box('Under development', "This part is not ready yet :)")
            elif mouse_click[0] and not bet and barrell_spin == True:
                draw_functions.draw_message_box('Bet error', "You need to place a bet first")
            elif mouse_click[0] and bet == True and not barrell_spin:
                draw_functions.draw_message_box('Spin error', "You need to spin the barrell first")
            elif mouse_click[0] and not bet and not barrell_spin:
                draw_functions.draw_message_box('Roulette error', "You need to place the bet and spin the barrell first")
       
        info = pygame.Rect(const.screen.get_width()-const.button_width-900, const.screen.get_height()-const.button_height+30, const.button_width+800, const.button_height-30)
        draw_functions.draw_button(const.screen, const.table_brown, info, info_text, font, const.white)
    
        pygame.display.flip()
    pygame.quit()
    exit()