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
elecs_bckgd = (53, 112, 61)
furniture_bckgd = (36, 35, 58)
clothing_bckgd = (63, 49, 67)
groceries_bckgd = (78, 120, 100)
tools_bckgd = (55, 111, 118)
safety_bckgd = (170, 207, 224)
power_bckgd = (47, 99, 135)
cars_bckgd = (0, 34, 48)
hatchback_bckgd = (221, 165, 58)
pickup_bckgd = (24, 64, 93)
acc_bckgd = (41, 105, 180)
consoles_bckgd = (226, 232, 232)
laptops_bckgd = (14, 37, 66)
smartpgones_bckgd = (78, 120, 158)
beds_bckgd = (228, 166, 59)
shelves_bckgd = (52, 90, 123)
pants_bckgd = (141, 81, 37)
snees_bckgd = (56, 46, 95)

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
STATE_ACCESSORIES = "accessories_section_screen"
STATE_CONSOLES = "consoles_section_screen"
STATE_LAPTOPS = "laptops_section_screen"
STATE_SMARTPHONES = "smartphones_section_screen"
STATE_ARMCHAIRS = "armchairs_section_screen"
STATE_BEDS = "beds_section_screen"
STATE_BOOKSHELVES = "bookshelves_section_screen"
STATE_TABLES = "tables_section_screen"
STATE_TSHIRT = "tshirt_section_screen"
STATE_HOODIE = "hoodie_section_screen"
STATE_PANTS = "pants_section_screen"
STATE_SNEES = "snees_Section_screen"
STATE_FRUITS =  "fruits_section_screen"
STATE_BREAD = "bread_section_screen"
STATE_VEGETABLES = "vegetables_section_screen"
STATE_MILK = "milk_section_screen"
STATE_HAND_TOOLS = "hand_tools_section_screen"
STATE_POWER_TOOLS = "power_tools_section_screen"
STATE_SAFETY_GEAR = "safety_gear_section_screen"
STATE_TOOLS_ACCESSORIES = "tool_accessories_section_screen"
STATE_SPORTS_CAR_1 = "sports_car_1"
STATE_SPORTS_CAR_2 = "sports_car_2"
STATE_SPORTS_CAR_3 = "sports_car_3"
STATE_SPORTS_CAR_4 = "sports_car_4"
STATE_SEDAN_CAR_1 = "sedan_car_1"
STATE_SEDAN_CAR_2 = "sedan_car_2"
STATE_SEDAN_CAR_3 = "sedan_car_3"
STATE_SEDAN_CAR_4 = "sedan_car_4"
STATE_SUV_CAR_1 = "suv_car_1"
STATE_SUV_CAR_2 = "suv_car_2"
STATE_SUV_CAR_3 = "suv_car_3"
STATE_SUV_CAR_4 = "suv_car_4"
STATE_PICKUP_CAR_1 = "pickup_car_1"
STATE_PICKUP_CAR_2 = "pickup_car_2"
STATE_PICKUP_CAR_3 = "pickup_car_3"
STATE_PICKUP_CAR_4 = "pickup_car_4"
STATE_HATCHBACK_CAR_1 = "hatchback_car_1"
STATE_HATCHBACK_CAR_2 = "hatchback_car_2"
STATE_HATCHBACK_CAR_3 = "hatchback_car_3"
STATE_HATCHBACK_CAR_4 = "hatchback_car_4"
STATE_CONSOLE_1 = "console_1"
STATE_CONSOLE_2 = "console_2"
STATE_CONSOLE_3 = "console_3"
STATE_CONSOLE_4 = "console_4"
STATE_ACC_1 = "acc_1"
STATE_ACC_2 = "acc_2"
STATE_ACC_3 = "acc_3"
STATE_ACC_4 = "acc_4"
STATE_LAPTOP_1 = "laptop_1"
STATE_LAPTOP_2 = "laptop_2"
STATE_LAPTOP_3 = "laptop_3"
STATE_LAPTOP_4 = "laptop_4"
STATE_SMARTPHONE_1 = "smartphone_1"
STATE_SMARTPHONE_2 = "smartphone_2"
STATE_SMARTPHONE_3 = "smartphone_3"
STATE_SMARTPHONE_4 = "smartphone_4"
STATE_CHAIR_1 = "chair_1"
STATE_CHAIR_2 = "chair_2"
STATE_CHAIR_3 = "chair_3"
STATE_CHAIR_4 = "chair_4"
STATE_BED_1 = "bed_1"
STATE_BED_2 = "bed_2"
STATE_BED_3 = "bed_3"
STATE_BED_4 = "bed_4"
STATE_SHELF_1 = "shelf_1"
STATE_SHELF_2 = "shelf_2"
STATE_SHELF_3 = "shelf_3"
STATE_SHELF_4 = "shelf_4"
STATE_TABLE_1 = "table_1"
STATE_TABLE_2 = "table_2"
STATE_TABLE_3 = "table_3"
STATE_TABLE_4 = "table_4"
STATE_HOODIE_1 = "hoodie_1"
STATE_HOODIE_2 = "hoodie_2"
STATE_HOODIE_3 = "hoodie_3"
STATE_HOODIE_4 = "hoodie_4"
STATE_PANTS_1 = "pants_1"
STATE_PANTS_2 = "pants_2"
STATE_PANTS_3 = "pants_3"
STATE_PANTS_4 = "pants_4"
STATE_SHOE_1 = "shoe_1"
STATE_SHOE_2 = "shoe_2"
STATE_SHOE_3 = "shoe_3"
STATE_SHOE_4 = "shoe_4"
STATE_TSHIRT_1 = "tshirt_1"
STATE_TSHIRT_2 = "tshirt_2"
STATE_TSHIRT_3 = "tshirt_3"
STATE_TSHIRT_4 = "tshirt_4"
STATE_HAND_TOOL_1 = "hand_tool_1"
STATE_HAND_TOOL_2 = "hand_tool_2"
STATE_HAND_TOOL_3 = "hand_tool_3"
STATE_HAND_TOOL_4 = "hand_tool_4"
STATE_ACCS_TOOL_1 = "accs_tool_1"
STATE_ACCS_TOOL_2 = "accs_tool_2"
STATE_ACCS_TOOL_3 = "accs_tool_3"
STATE_ACCS_TOOL_4 = "accs_tool_4"
STATE_POWER_TOOL_1 = "power_tool_1"
STATE_POWER_TOOL_2 = "power_tool_2"
STATE_POWER_TOOL_3 = "power_tool_3"
STATE_POWER_TOOL_4 = "power_tool_4"
STATE_SAFETY_TOOL_1 = "safety_tool_1"
STATE_SAFETY_TOOL_2 = "safety_tool_2"
STATE_SAFETY_TOOL_3 = "safety_tool_3"
STATE_SAFETY_TOOL_4 = "safety_tool_4"

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