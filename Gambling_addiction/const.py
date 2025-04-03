import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Gambling addiction')

#Balance, should later be saved and loaded from the txt file
balance = 500
bet = ""

# Colours
white = (255, 255, 255)
blue = (0, 0, 200)
red = (255, 0, 0)
hover_blue = (0, 0, 255)
text_blue = (0, 0, 128)
black = (0, 0, 0)
green = (1, 107, 50)
brown = (92, 64, 51)

#Buttons
button_width = 300
button_height = 80

#Text
start_screen_info = "Welcome traveller, here is a little starting information about the game here: There are two types of game for you to play: " \
    "Russian roulette and basic casino roulette. I assume you already know what the difference between these two is, but in case you are" \
    "not aware, here is a little explanation for you: " \
    "1)Russian roulette: its a 2 player game, you play it with the pistol and 1 bullet that can be in 1 of the six chambers, whoever dies first, losses the game. " \
    "2)Casino roulette: table, ball and spinning wheel, if you manage to guess the proper number, you win, if not, you losse. " \
    "To continue press start button"

casino_screen_message_box = "Welcome to Gambling Addiction Casion, your luck is our money, here is a little explanation on how this works:\n" \
"There are multiple variables: balance - represents your current bank balance and max amount of money you can bet\n" \
"your_bet - the amount of money that you bet\n others_bet - the amount of money other people bet in total\n " \
"table - current amount of money on the table that you can win if you guess correct number and colour\n " \
"your_number/combination - number/combination that you put your bet on\n your_colour - colour that you bet on\n to_win - the amount you can win in this spin\n " \
"If you bet only on number, and guess it correctly, you can win 35x the amount of the money you bet\n if you guess colour " \
"and number correctly, you can win all the money on the table\n if you guess only colour correctly, you can win the same amount you bet, on top of what you " \
"put on the table\n if you split the bet between two numbers, you can win 17x the amount you bet\n if you split it between 3 numbers, you can win 11x the bet\n " \
"if you split it between four numbers, you can win 8x the amount you bet\n if you split it between 6 numbers, you can win 5x the amount of bet\n if you play " \
"0 + 2 other numbers, you can win 11x the amount you bet\n if you play even/odd, you can win the same amount you bet\n if you play low/high (1 - 18/19 - 36) " \
"you earn same amount you bet\n if you play dozens (1 - 12, 13 - 24, 25 - 36), you earn double the amount you bet"

game_screen1_text = f"You are chilling at your home, your current bank balance is {balance} dollars, what do you want to do"

choice_info_text = "(1) Number only - If you bet only on number, and guess it correctly, you can win 35x the amount of the money you bet\n" \
"(2) Colour and number - you can win all the money on the table\n" \
"(3) Only colour - if you guess only colour correctly, you can win the same amount you bet, on top of what you put on the table\n" \
"(4) Two numbers - if you split the bet between two numbers, you can win 17x the amount you bet\n" \
"(5) Three numbers - if you split it between 3 numbers, you can win 11x the bet\n(6) Four numbers - if you split it between four numbers, you can win 8x the amount you bet\n" \
"(7) Six numbers - if you split it between 6 numbers, you can win 5x the amount of bet\n(8) 0 + 2 - you can win 11x the amount you bet\n" \
"(9) Even/Odd -if you play even/odd, you can win the same amount you bet\n " \
"(10) Low/High - if you play low/high (1 - 18/19 - 36) you earn same amount you bet\n" \
"(11) Dozens - if you play dozens (1 - 12, 13 - 24, 25 - 36), you earn double the amount you bet\n"

#States
STATE_CITY = "city"
STATE_APARTMENT = "apartment"
STATE_CASINO = "casino"
STATE_EXIT_APARTMENT = "exit_door"
STATE_WORK = "work"

#Check list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']