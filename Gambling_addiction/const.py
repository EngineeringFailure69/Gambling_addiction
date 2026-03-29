import pygame
import utils.file_utils as file_utils
import utils.utils as utils
from utils.utils import* #buy_product
import interface.city_screen as city_screen
import interface.apartment_screen as apartment_screen
import interface.casino_screen as casino_screen
import interface.job_interface.work_screen as work_screen
import interface.russian_roulette_screen as russian_roulette_screen
import interface.shopping_interface.shopping_center_screen as shopping_center_screen
import interface.shopping_interface.cars_section.cars_screen as cars_screen
import interface.shopping_interface.electronics_section.electronics_screen as electronics_screen
import interface.shopping_interface.furniture_section.furniture_screen as furniture_screen
import interface.shopping_interface.clothing_section.clothing_screen as clothing_screen
import interface.shopping_interface.tools_section.tools_screen as tools_screen
import interface.shopping_interface.groceries_section.groceries_screen as groceries_screen
import interface.shopping_interface.cars_section.sedan_car_section_screen as sedan_car_section_screen
import interface.shopping_interface.cars_section.sports_car_section_screen as sports_car_section_screen
import interface.shopping_interface.cars_section.pickup_car_section_screen as pickup_car_section_screen
import interface.shopping_interface.cars_section.hatchback_car_section_screen as hatchback_car_section_screen
import interface.shopping_interface.cars_section.suv_car_section_screen as suv_car_section_screen
import interface.shopping_interface.electronics_section.accessories_section_screen as accessories_section_screen
import interface.shopping_interface.electronics_section.consoles_section_screen as consoles_section_screen
import interface.shopping_interface.electronics_section.laptops_section_screen as laptops_section_screen
import interface.shopping_interface.electronics_section.smartphones_section_screen as smartphones_section_screen
import interface.shopping_interface.furniture_section.armchairs_section_screen as armchairs_section_screen
import interface.shopping_interface.furniture_section.tables_section_screen as tables_section_screen
import interface.shopping_interface.furniture_section.beds_section_screen as beds_section_screen
import interface.shopping_interface.furniture_section.bookshleves_section_screen as bookshleves_section_screen
import interface.shopping_interface.clothing_section.hoodie_section_screen as hoodie_section_screen
import interface.shopping_interface.clothing_section.pants_section_screen as pants_section_screen
import interface.shopping_interface.clothing_section.snees_section_screen as snees_section_screen
import interface.shopping_interface.clothing_section.tshirt_section_screen as tshirt_section_screen
import interface.shopping_interface.groceries_section.fruits_section_screen as fruits_section_screen
import interface.shopping_interface.groceries_section.bread_section_screen as bread_section_screen
import interface.shopping_interface.groceries_section.milk_section_screen as milk_section_screen
import interface.shopping_interface.groceries_section.vegetables_section_sceen as vegetables_section_screen
import interface.shopping_interface.tools_section.hand_tools_section_screen as hand_tools_section_screen
import interface.shopping_interface.tools_section.power_tools_section_screen as power_tools_section_screen
import interface.shopping_interface.tools_section.safety_gear_section_screen as safety_gear_section_screen
import interface.shopping_interface.tools_section.tools_accessories_section_screen as tools_accessories_section_screen
import interface.shopping_interface.electronics_section.accessories_section_screen as accessories_section_screen
import interface.shopping_interface.electronics_section.consoles_section_screen as consoles_section_screen
import interface.shopping_interface.electronics_section.laptops_section_screen as laptops_section_screen
import interface.shopping_interface.electronics_section.smartphones_section_screen as smartphones_section_screen
import interface.shopping_interface.furniture_section.armchairs_section_screen as armchairs_section_screen
import interface.shopping_interface.furniture_section.beds_section_screen as beds_section_screen
import interface.shopping_interface.furniture_section.bookshleves_section_screen as bookshleves_section_screen
import interface.shopping_interface.furniture_section.tables_section_screen as tables_section_screen
import settings_screen as settings_screen

pygame.init()
screen = pygame.display.set_mode((1400, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Gambling addiction')

#Buttons
button_width = 300
button_height = 80
button_center_x = const.screen.get_width()/2-const.button_width/2
import const

#door icon
door_icon_path = "icons\\door_icon.webp"
door_icon_width = 75
door_icon_height = 75
door_icon_position_x = const.screen.get_width()-100
door_icon_position_y = const.screen.get_height()-80

#shopping icon
shopping_icon_path = "icons\\shopping_icon.svg"
shopping_icon_width = 70
shopping_icon_height = 70
shopping_icon_position_x = const.screen.get_width()/47
shopping_icon_position_y = const.screen.get_height()-80

#work icon
work_icon_path = "icons\\work_icon.webp"
work_icon_width = 70
work_icon_height = 70
work_icon_position_x = const.screen.get_width()/47
work_icon_position_y = const.screen.get_height()-80

#settings icon
settings_icon_path = "icons\\settings_icon.png"
settings_icon_width = 100
settings_icon_height = 70
settings_icon_position_x = 1300
settings_icon_position_y = 10

#shop_fps_show 
fps_rect = pygame.Rect(10, 10, 120, 20)
fps = 60
line_spacing = 5
 
#Often used UI elements
bet_button = pygame.Rect(screen.get_width()/60, screen.get_height()//50, button_width-250, button_height-50)
your_bet_box = pygame.Rect(screen.get_width()/60 + bet_button.width + 20, screen.get_height()//50, button_width, button_height-50)
pick_colour_button = pygame.Rect(screen.get_width()-710, screen.get_height()//50, button_width-200, button_height-50)
red_colour_button = pygame.Rect(screen.get_width()-600, screen.get_height()//50, button_width-250, button_height-50)
black_colour_button = pygame.Rect(screen.get_width()-770, screen.get_height()//50, button_width-250, button_height-50)
choice_Info_button = pygame.Rect(screen.get_width()-230, screen.get_height()//50, button_width-150, button_height-50)
right_choice_button = pygame.Rect(screen.get_width()-300, screen.get_height()//50, button_width-250, button_height-50)
left_choice_button = pygame.Rect(screen.get_width()-520, screen.get_height()//50, button_width-250, button_height-50)
choice_button = pygame.Rect(screen.get_width()-460, screen.get_height()//50, button_width-150, button_height-50)
buy_Info_button = pygame.Rect(screen.get_width()-210, screen.get_height()//50, button_width-150, button_height-50)

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

pull_the_trigger_button = pygame.Rect(screen.get_width()-250, screen.get_height()//50, button_width-150, button_height-50)
spin_the_barrell_button = pygame.Rect(screen.get_width()-570, screen.get_height()//50, button_width, button_height-50)

info = pygame.Rect(0, screen.get_height()-button_height+30, screen.get_width()-200, button_height-30)
apply_button = pygame.Rect(screen.get_width()/2-button_width/2, screen.get_height()-(screen.get_height()/3), button_width, button_height) 

inventory_button = pygame.Rect(screen.get_width()-240, screen.get_height()//50, button_width-150, button_height-50)

text_rect = pygame.Rect(10, const.screen.get_height() / 13, screen.get_width(), 300)

save_path = file_utils.extract_default_save()
balance = file_utils.load_save_game_info("save_files\\information.txt", "balance")
balance = float(balance)
salary = file_utils.load_save_game_info(save_path, "salary")
salary = int(salary)
bet = ""
your_bet = 0
working = file_utils.load_save_game_info(save_path, "working")
working = int(working)

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
bread_bckgd = (59, 120, 173)
fruit_bckg = (100, 160, 185)
vegetables_bckgd = (251, 231, 198)
milk_bckgd = (255, 207, 134)
 
#States
STATE_APARTMENT = apartment_screen.apartment_screen
STATE_CASINO = casino_screen.casino_screen
STATE_TO_THE_STREETS = city_screen.city_screen
STATE_WORK = work_screen.work_screen
STATE_RUSSIAN_ROULETTE = russian_roulette_screen.russian_roulette_screen
STATE_SHOPPING = shopping_center_screen.shopping_center_screen
STATE_CARS = cars_screen.cars_screen
STATE_ELECTRONICS = electronics_screen.electronics_screen
STATE_FURNITURE = furniture_screen.furniture_screen
STATE_CLOTHING = clothing_screen.clothing_screen
STATE_TOOLS = tools_screen.tools_screen
STATE_GROCERIES = groceries_screen.groceries_screen
STATE_SPORTS_CAR = sports_car_section_screen.sports_car_section_screen
STATE_SUV = suv_car_section_screen.suv_car_section_screen
STATE_HATCHBACK = hatchback_car_section_screen.hatchback_car_section_screen
STATE_SEDAN = sedan_car_section_screen.sedan_car_section_screen
STATE_PICKUP = pickup_car_section_screen.pickup_car_section_screen
STATE_ACCESSORIES = accessories_section_screen.accessories_section_screen
STATE_CONSOLES = consoles_section_screen.consoles_section_screen
STATE_LAPTOPS = laptops_section_screen.laptops_section_screen
STATE_SMARTPHONES = smartphones_section_screen.smartphones_section_screen
STATE_ARMCHAIRS = armchairs_section_screen.armchairs_section_screen
STATE_BEDS = beds_section_screen.beds_section_screen
STATE_BOOKSHELVES = bookshleves_section_screen.bookshelves_section_screen
STATE_TABLES = tables_section_screen.tables_section_screen
STATE_TSHIRT = tshirt_section_screen.tshirt_section_screen
STATE_HOODIE = hoodie_section_screen.hoodie_section_screen
STATE_PANTS = pants_section_screen.pants_section_screen
STATE_SNEES = snees_section_screen.snees_section_screen
STATE_FRUITS  =  fruits_section_screen.fruits_section_screen
STATE_BREAD = bread_section_screen.bread_section_screen
STATE_VEGETABLES = vegetables_section_screen.vegetables_section_screen
STATE_MILK = milk_section_screen.milk_section_screen
STATE_HAND_TOOLS = hand_tools_section_screen.hand_tools_section_screen
STATE_POWER_TOOLS = power_tools_section_screen.power_tools_section_screen
STATE_SAFETY_GEAR = safety_gear_section_screen.safety_gear_section_screen
STATE_TOOLS_ACCESSORIES = tools_accessories_section_screen.tools_accessories_section_screen
STATE_BUY_PRODUCT = buy_product_and_add_to_the_inventory
STATE_SETTINGS = settings_screen.settings_screen

#list with all state names and all functions connected to them (its filled in automatically, no need to touch)
screen_and_buy_functions = {}

#Image/icons caching dictionary
images_cache = {}

#Check list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_counter = 0

#russian roulette parameters
bullet_chamber = 0
current_chamber = 0
round_counter = 0
barrel = []
current_chamber = 0

day_counter = file_utils.load_save_game_info("save_files\\information.txt", "day_counter")
day_counter = int(day_counter)
month_counter = file_utils.load_save_game_info("save_files\\information.txt", "month_counter")
month_counter = int(month_counter)
year_counter = file_utils.load_save_game_info("save_files\\information.txt", "year_counter")
year_counter = int(year_counter)
date_time_ms = 0
return_day_counter = file_utils.load_save_game_info("save_files\\information.txt", "return_day_counter")
return_day_counter = int(return_day_counter)
return_month_counter = file_utils.load_save_game_info("save_files\\information.txt", "return_month_counter")
return_month_counter = int(return_month_counter)
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
index = int(index)

buttons_list = []
tes = False
job_apply = False 

inventory_list_file = file_utils.load_list_from_file(save_path, "inventory_list") 
inventory_list = utils.load_inventory_objects()
inventory_index = 0

#settings data
fps_show = True
fps_apply = True
pygame.mixer.init()
playlist = utils.grab_all_sounds_from_the_music_drectory()#[]#["C:\\Users\\Windows\\Desktop\\mixkit-game-level-music-689.wav"]

current_song_index = 0 
MUSIC_END = pygame.USEREVENT + 1