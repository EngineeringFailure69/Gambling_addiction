import random
import const

def to_win(your_bet):
    return your_bet * 100

def spin_the_barrell():
    const.barrel = [False] * 6
    const.barrel[random.randint(0, 5)] = True
    const.current_chamber = random.randint(0, 5)
    print(const.barrel)
    print(const.current_chamber)

def roll_the_dice(you_play):
    roll_player = random.randint(1, 6)
    roll_opponent = random.randint(1, 6)
    if roll_player >= roll_opponent:
        you_play = True
    elif roll_player < roll_opponent:
        you_play = False 
    return you_play, roll_player, roll_opponent

def pull_the_trigger(you_play):
    if const.current_chamber >= len(const.barrel):
        const.current_chamber = 0
    if const.barrel[const.current_chamber] == True and you_play == True:
        you_play = not you_play
        const.current_chamber += 1
        return False, True, you_play  # You lost (you are dead mate) - 1st false, 2nd true is that game is over
    elif const.barrel[const.current_chamber] == True and you_play == False:
        const.current_chamber += 1
        you_play = not you_play
        return True, True, you_play  # You won (you are alive hehe)
    elif const.barrel[const.current_chamber] == False and you_play == False:
        const.current_chamber += 1
        you_play = not you_play
        return False, False, you_play #Your opponent survived, you pull the trigger next
    elif const.barrel[const.current_chamber] == False and you_play == True:
        const.current_chamber += 1
        you_play = not you_play
        return False, False, you_play #You survived, your opponent pulls the trigger next