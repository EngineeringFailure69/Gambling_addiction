import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Gambling addiction')

# Colours
white = (255, 255, 255)
blue = (0, 0, 200)
red = (255, 0, 0)
hover_blue = (0, 0, 255)
text_blue = (0, 0, 128)
black = (0, 0, 0)

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

balance = 500

game_screen1_text = f"You are chilling at your home, your current bank balance is {balance} dollars, what do you want to do"