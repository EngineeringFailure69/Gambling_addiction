import random
import time

def to_win_function(choice, your_bet, your_colour, your_numbers = []):
    others_bet = random.randint(your_bet, 10*your_bet)
    table = your_bet + others_bet
    your_colour = your_colour.lower()

    if(choice == 1):
        your_colour = "none"
        to_win = your_bet + your_bet * 35
    elif(choice==2):
        if(your_colour == "black" or your_colour == "red"):
            to_win = table
        else: 
            print("Colour does not exists")
    elif(choice==3):
        your_numbers = []
        your_numbers.append(-1)
        if(your_colour == "black" or your_colour == "red"):
            to_win = your_bet * 2
        else: 
            print("Colour does not exists")
    elif(choice==4):
        your_colour = "none"
        to_win = your_bet + your_bet * 17
    elif(choice==5):
        your_colour = "none"
        to_win = your_bet + your_bet * 11
    elif(choice==6):
        your_colour = "none"
        to_win = your_bet + your_bet * 8
    elif(choice==7):
        your_colour = "none"
        to_win = your_bet + your_bet * 5
    elif(choice==8):
        your_colour = "none"
        to_win = your_bet + your_bet * 11
    elif(choice==9):
        your_colour = "none"
        to_win = your_bet * 2
    elif(choice==10): 
        your_colour = "none"
        to_win = your_bet * 2
    elif(choice==11): 
        your_colour = "none"
        to_win = your_bet + (your_bet*2)

    return to_win, others_bet, table, your_colour

def casino_roulette(balance, your_bet, choice, your_colour, your_numbers = []):
    to_win,  others_bet, table, your_colour = to_win_function(choice, your_bet, your_colour, your_numbers)
    
    print(f"Your balance: {balance}", "\t", f"Your bet: {your_bet}", "\t", f"Your number: {your_numbers}", "\t", f"Your colour: {your_colour}") 
    print(f"Others bet: {others_bet}", "\t", f"Sum on the table: {table}", "\t", f"Amount that you can win: {to_win}", "\n")
    print("Spinning the wheel...")
    won = True
    spin = random.randint(0, 36)
    spin_colour = random.choice(["red", "black"])
    print(f"Number that it fell on: {spin}\nColour that it fell on: {spin_colour}")
    if(your_colour == "none" and spin in your_numbers):
        balance = balance + to_win
    elif(your_colour == spin_colour and spin in your_numbers):
        balance += to_win
    elif(your_colour == spin_colour and spin not in your_numbers):
        balance += to_win
    else:
        print(f"You lost: {your_bet} dollars")
        won = False
        balance -= your_bet
    return balance, to_win, table, won, your_colour, spin, spin_colour