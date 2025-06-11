import pygame
import utils.file_utils as file_utils

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

info = pygame.Rect(0, screen.get_height()-button_height+30, screen.get_width()-200, button_height-30)
apply_button = pygame.Rect(screen.get_width()/2-button_width/2, screen.get_height()-(screen.get_height()/3), button_width, button_height) 

save_path = file_utils.extract_default_save()
balance = file_utils.load_save_game_info("save_files\information.txt", "balance")
salary = file_utils.load_save_game_info(save_path, "salary")
bet = ""
your_bet = 0
working = file_utils.load_save_game_info(save_path, "working")

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
store_bckgd = (250, 237, 216)
store_text = (25, 69, 89)

#States
STATE_CITY = "city"
STATE_APARTMENT = "apartment"
STATE_CASINO = "casino"
STATE_TO_THE_STREETS = "exit_door"
STATE_WORK = "work"
STATE_RUSSIAN_ROULETTE = "russian_roulette"
STATE_SHOPPING = "shopping_center"
STATE_CARS = "cars_screen"
STATE_ELECTRONICS = "electronics_screen"
STATE_FURNITURE = "furniture_screen"
STATE_CLOTHING = "clothing_screen"
STATE_TOOLS = "tools_screen"
STATE_GROCERIES = "groceries_screen"
STATE_SPORTS_CAR = "sports_car_section_screen"
STATE_SUV = "suv_section_screen"
STATE_HATCHBACK = "hatchback_section_screen"
STATE_SEDAN = "sedan_section_screen"
STATE_PICKUP = "pickup_section_screen"

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
    ["Slot Attendant", 2500, "Assists with slot machines"],
    ["Dealer", 3500, "Conducts table games and manages plays"],
    ["Shift Lead", 4500, "Ovresees dealers and floor personnel"], 
    ["Pit Boss", 6000, "Supervises floor staff"],
    ["Shift Manager", 7500, "Assists in in managing casino"],
    ["Manager", 10000, "You control everything in the casino"],
]

job_positions_list = file_utils.load_list_from_file(save_path, "job_positions_list")
index = file_utils.load_save_game_info(save_path, "index") #0

buttons_list = []
tes = False
job_apply = False