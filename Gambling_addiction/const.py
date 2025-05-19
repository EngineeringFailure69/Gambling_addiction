import pygame
import file_utils

pygame.init()
screen = pygame.display.set_mode((1400, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Gambling addiction')

#Buttons
button_width = 300
button_height = 80

#Often used UI elements
bet_button = pygame.Rect(screen.get_width()/60, screen.get_height()//50, button_width-250, button_height-50)
your_bet_box = pygame.Rect(screen.get_width()/60 + bet_button.width + 20, screen.get_height()//50, button_width, button_height-50)
pick_colour_button = pygame.Rect(screen.get_width()-710, screen.get_height()//50, button_width-200, button_height-50)
red_colour_button = pygame.Rect(screen.get_width()-600, screen.get_height()//50, button_width-250, button_height-50)
black_colour_button = pygame.Rect(screen.get_width()-770, screen.get_height()//50, button_width-250, button_height-50)
choice_Info_button = pygame.Rect(screen.get_width()-180, screen.get_height()//50, button_width-150, button_height-50)
right_choice_button = pygame.Rect(screen.get_width()-300, screen.get_height()//50, button_width-250, button_height-50)
left_choice_button = pygame.Rect(screen.get_width()-520, screen.get_height()//50, button_width-250, button_height-50)
choice_button = pygame.Rect(screen.get_width()-460, screen.get_height()//50, button_width-150, button_height-50)

right_choice1_button = pygame.Rect(screen.get_width()-300, screen.get_height()//10, button_width-250, button_height-50)
left_choice1_button = pygame.Rect(screen.get_width()-520, screen.get_height()//10, button_width-250, button_height-50)
choice1_button = pygame.Rect(screen.get_width()-460, screen.get_height()//10, button_width-150, button_height-50)

right_choice2_button = pygame.Rect(screen.get_width()-300, screen.get_height()//5.5, button_width-250, button_height-50)
left_choice2_button = pygame.Rect(screen.get_width()-520, screen.get_height()//5.5, button_width-250, button_height-50)
choice2_button = pygame.Rect(screen.get_width()-460, screen.get_height()//5.5, button_width-150, button_height-50)

right_choice3_button = pygame.Rect(screen.get_width()-300, screen.get_height()//3.8, button_width-250, button_height-50)
left_choice3_button = pygame.Rect(screen.get_width()-520, screen.get_height()//3.8, button_width-250, button_height-50)
choice3_button = pygame.Rect(screen.get_width()-460, screen.get_height()//3.8, button_width-150, button_height-50)

right_choice4_button = pygame.Rect(screen.get_width()-300, screen.get_height()//2.9, button_width-250, button_height-50)
left_choice4_button = pygame.Rect(screen.get_width()-520, screen.get_height()//2.9, button_width-250, button_height-50)
choice4_button = pygame.Rect(screen.get_width()-460, screen.get_height()//2.9, button_width-150, button_height-50)

right_choice5_button = pygame.Rect(screen.get_width()-300, screen.get_height()//2.35, button_width-250, button_height-50)
left_choice5_button = pygame.Rect(screen.get_width()-520, screen.get_height()//2.35, button_width-250, button_height-50)
choice5_button = pygame.Rect(screen.get_width()-460, screen.get_height()//2.35, button_width-150, button_height-50)

right_choice6_button = pygame.Rect(screen.get_width()-300, screen.get_height()//2, button_width-250, button_height-50)
left_choice6_button = pygame.Rect(screen.get_width()-520, screen.get_height()//2, button_width-250, button_height-50)
choice6_button = pygame.Rect(screen.get_width()-460, screen.get_height()//2, button_width-150, button_height-50)

pull_the_trigger_button = pygame.Rect(screen.get_width()-180, screen.get_height()//50, button_width-150, button_height-50)
spin_the_barrell_button = pygame.Rect(screen.get_width()-510, screen.get_height()//50, button_width, button_height-50)

#Balance, should later be saved and loaded from the txt file
balance = file_utils.load_save_game_info("save_files\information.txt", "balance")
bet = ""
your_bet = 0

# Colours
white = (255, 255, 255)
blue = (0, 0, 200)
red = (255, 0, 0)
hover_blue = (0, 0, 255)
text_blue = (0, 0, 128)
black = (0, 0, 0)
green = (1, 107, 50)
brown = (92, 64, 51)
table_brown = (45, 25, 15)
job_box = (243, 213, 168)
job_title = (254, 195, 102)
job_button = (230, 192, 137)
job_cards_text = (74, 40, 15)

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

game_screen1_text = f"You are chilling at your home, what do you want to do, your current bank balance is: "

choice_info_text = "(1) Number only - If you bet only on number, and guess it correctly, you can win 35x the amount of the money you bet\n" \
"(2) Colour and number - you can win all the money on the table\n" \
"(3) Only colour - if you guess only colour correctly, you can win the same amount you bet, on top of what you put on the table\n" \
"(4) Two numbers - if you split the bet between two numbers, you can win 17x the amount you bet\n" \
"(5) Three numbers - if you split it between 3 numbers, you can win 11x the bet\n(6) Four numbers - if you split it between four numbers, you can win 8x the amount you bet\n" \
"(7) Six numbers - if you split it between 6 numbers, you can win 5x the amount of bet\n(8) 0 + 2 - you can win 11x the amount you bet\n" \
"(9) Even/Odd -if you play even/odd, you can win the same amount you bet\n " \
"(10) Low/High - if you play low/high (1 - 18/19 - 36) you earn same amount you bet\n" \
"(11) Dozens - if you play dozens (1 - 12, 13 - 24, 25 - 36), you earn double the amount you bet\n"

russian_roulette_text = "This is a russian roulette commrade, you win or you die, if you win, you get up to x100 what you bet, if you lose, well, you know what happens"
barrel_text = "Spinning the barrell..."
dice_text = "While the barrell was spinning, the dice was rolled, first roll represents your number, " \
"2nd roll represents your opponent number, whoever gets bigger number, plays first, the result: "

#States
STATE_CITY = "city"
STATE_APARTMENT = "apartment"
STATE_CASINO = "casino"
STATE_TO_THE_STREETS = "exit_door"
STATE_WORK = "work"
STATE_RUSSIAN_ROULETTE = "russian_roulette"

#Check list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_counter = 0

#russian roulette parameters
bullet_chamber = 0
current_chamber = 0
round_counter = 0
barrel = []
current_chamber = 0

day_counter = file_utils.load_save_game_info("save_files\information.txt", "day_counter")
month_counter = file_utils.load_save_game_info("save_files\information.txt", "month_counter")
year_counter = file_utils.load_save_game_info("save_files\information.txt", "year_counter")
date_time_ms = 0
return_day_counter = file_utils.load_save_game_info("save_files\information.txt", "return_day_counter")
return_month_counter = file_utils.load_save_game_info("save_files\information.txt", "return_month_counter")
leap_year = False

#jobs
jobs_list = [
    ["Janitor", 300, "You keep the casino clean"],
    ["Waiter", 800, "You serve drinks to the guests"],
    ["Bartender", 1200, "You oversee the operations on the floor"],
    ["Security", 2000, "You protect the casino"],
    ["Manager", 5000, "You control everything in the casino"],
]