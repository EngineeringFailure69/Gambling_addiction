import random
import const

def to_win(your_bet):
    return your_bet * 100

def spin_the_barrell():
    const.bullet_chamber = random.randint(1, 6)
    const.current_chamber = random.randint(1, 6)

def roll_the_dice(you_play_first):
    roll_player = random.randint(1, 6)
    roll_opponent = random.randint(1, 6)
    if roll_player >= roll_opponent:
        you_play_first = True
    elif roll_player < roll_opponent:
        you_play_first = False 
    return you_play_first, roll_player, roll_opponent

def pull_the_trigger(you_play_first):
    const.current_chamber += 1
    if const.current_chamber == const.bullet_chamber and you_play_first:
        return True
    elif const.current_chamber > 6:
        const.current_chamber = 1
    elif const.current_chamber == const.bullet_chamber and not you_play_first:
        return False