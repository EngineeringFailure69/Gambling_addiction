import random
import const

def to_win(your_bet):
    return your_bet * 100

def spin_the_barrell():
    const.bullet_chamber = random.randint(1, 6)
    const.current_chamber = random.randint(1, 6)