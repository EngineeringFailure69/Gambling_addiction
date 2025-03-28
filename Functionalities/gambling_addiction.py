import random
import time

def to_win_function(choice, your_bet):
    others_bet = random.randint(your_bet, 10*your_bet)
    table = your_bet + others_bet
    your_numbers = []

    if(choice == 1):
        your_numbers.append(int(input("Enter the number you want to bet on: ")))
        your_colour = "none"
        to_win = your_bet + your_bet * 35
    elif(choice==2):
        your_numbers.append(int(input("Enter the number you want to bet on: ")))
        your_colour = input("Enter the colour that you want to bet on, or enter none: ")
        if(your_colour == "black" or your_colour == "red"):
            to_win = table
        else: 
            print("Colour does not exists")
    elif(choice==3):
        your_colour = input("Enter the colour that you want to bet on, or enter none: ")
        your_numbers.append(-1)
        if(your_colour == "black" or your_colour == "red"):
            to_win = your_bet * 2
        else: 
            print("Colour does not exists")
    elif(choice==4):
        your_colour = "none"
        for i in range(2):
            your_numbers.append(int(input(f"Enter the {i+1}st/nd number you want to bet on: ")))
        to_win = your_bet + your_bet * 17
    elif(choice==5):
        your_colour = "none"
        for i in range(3):
            your_numbers.append(int(input(f"Enter the {i+1}st/nd/rd number you want to bet on: ")))
        to_win = your_bet + your_bet * 11
    elif(choice==6):
        your_colour = "none"
        for i in range(4):
            your_numbers.append(int(input(f"Enter the {i+1}st/nd/rd/th number you want to bet on: ")))
        to_win = your_bet + your_bet * 8
    elif(choice==7):
        your_colour = "none"
        for i in range(6):
            your_numbers.append(int(input(f"Enter the {i+1}st/nd/rd/th number you want to bet on: ")))
        to_win = your_bet + your_bet * 5
    elif(choice==8):
        your_colour = "none"
        your_numbers.append(0)
        for i in range(2):
            your_numbers.append(int(input(f"Enter the {i+1}st/nd number you want to bet on: ")))
        to_win = your_bet + your_bet * 11
    elif(choice==9):
        your_colour = "none"
        evenodd = input("Do you want to bet on all even, or all odd numbers?: ")
        evenodd.lower()
        if(evenodd == "even"):
            for i in range(0, 37):
                if(i%2==0):
                    your_numbers.append(i)
        elif(evenodd == "odd"):
            for i in range(1, 36):
                if(i%2!=0):
                    your_numbers.append(i)
        else:
            print("You need to type even or odd")
        to_win = your_bet * 2
    elif(choice==10): 
        your_colour = "none"
        lowhigh = input("Do you want to play low (1-18) or high (19 - 36)?: ")
        lowhigh.lower()
        if(lowhigh == "low"):
            for i in range(1, 19):
                your_numbers.append(i)
        elif(lowhigh=="high"):
            for i in range(19, 37):
                your_numbers.append(i)
        else:
            print("You need to type low or high")
        to_win = your_bet * 2
    elif(choice==11): 
        your_colour = "none"
        dozens = int(input("Press enter and 1 if you want to play numbers 1-12, 2 if you want to play 13-24, 3 if you want to play 25-36: "))
        if(dozens==1):
            for i in range(1, 13):
                your_numbers.append(i)
        elif(dozens==2):
            for i in range(13, 25):
                your_numbers.append(i)
        elif(dozens==2):
            for i in range(25, 37):
                your_numbers.append(i)
        to_win = your_bet + (your_bet*2)

    return to_win, others_bet, table, your_numbers, your_colour


def casino_roulette(balance):
    print("Welcome to Gambling Addiction Casion, your luck is our money, here is a little explanation on how this works:")
    print("There are multiple variables:\nbalance - represents your current bank balance and max amount of money you can bet")
    print("your_bet - the amount of money that you bet\nothers_bet - the amount of money other people bet in total")
    print("table - current amount of money on the table that you can win if you guess correct number and colour")
    print("your_number - number that you put your bet on\nyour_colour - colour that you bet on\nto_win - the amount you can win in this spin")
    print("If you bet only on number, and guess it correctly, you can win 35x the amount of the money you bet, if you guess colour", end='')
    print("and number correctly, you can win all the money on the table, if you guess only colour correctly, you can win the same amount you bet, on top of what you", end='')
    print("put on the table, if you split the bet between two numbers, you can win 17x the amount you bet, if you split it between 3 numbers, you can win 11x the bet", end='')
    print("if you split it between four numbers, you can win 8x the amount you bet, if you split it between 6 numbers, you can win 5x the amount of bet, if you play", end='')
    print("0 + 2 other numbers, you can win 11x the amount you bet, if you play even/odd, you can win the same amount you bet, if you play low/high (1 - 18/19 - 36)", end='')
    print("you earn same amount you bet, if you play dozens (1 - 12, 13 - 24, 25 - 36), you earn double the amount you bet")

    print("balance: ", balance)
    play = input("Do you want to play (type 1 and press enter) or not (type 2 and press enter)?: ")
    while(play!='1' and play!='2'):
        print("Its 1 or 2, not some random number, its not that hard man")
        play = int(input("Do you want to play (type 1 and press enter)?: "))
    while(play=='1'):
        your_bet = int(input("Enter the amount you want to bet: "))
        balance -= your_bet
        print("(1) Number only\n(2) Colour and number\n(3) Only colour\n(4) Two numbers\n(5) Three numbers\n(6) Four numbers\n(7) Six numbers\n(8) 0 + 2\n(9) Even/Odd")
        print("(10) Low/High\n(11) Dozens")
        choice = int(input("Pick the type of bet, enter the number inside () and press enter: "))
        your_numbers = []
        to_win,  others_bet, table, your_numbers, your_colour = to_win_function(choice, your_bet)
        
        spin = int(input("Ready to spin, if yes press 1 and enter: "))
        print(f"Your balance: {balance}", "\t", f"Your bet: {your_bet}", "\t", f"Your number: {your_numbers}", "\t", f"Your colour: {your_colour}") 
        print(f"Others bet: {others_bet}", "\t", f"Sum on the table: {table}", "\t", f"Amount that you can win: {to_win}", "\n")
        if(spin == 1):
            print("Spinning the wheel...")
            time.sleep(5)
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
        play = input(f"If you want to continue to play, type 1 and press enter, if not, type anything else and press enter, your current balance is {balance}: ")
    return balance

def russian_roulette():
    print("Win or die commrade, lets do this\n")
    return 

def main():
    print("Welcome traveller, here is a little starting information about the game here:\nThere are two types of game for you to play:") 
    print("Russian roulette and basic casion roulette. I assume you already know what the difference between these two is, but in case you are not aware, here is a little explanation for you:")
    print("1)Russian roulette: its a 2 player game, you play it with the pistol and 1 bullet that can be in 1 of the six chambers, whoever dies first, losses the game.")
    print("2)Casino roulette: table, ball and spinning wheel, if you manage to guess the proper number, you win, if not, you lose.")
    start = int(input("To continue press 1 and after that enter: "))
    condition = True
    balance = 500
    if(start == 1):
        print(f"You are chilling at your home, your current bank balance is {balance} dollars, what do you want to do:", end=' ')
        while condition:
            choice = int(input("Go to casino and play roulette (press 1 and enter) or go and play Russian roulette (press 2 and enter): "))
            if(choice == 1):
                balance = casino_roulette(balance)
                #condition = False
            elif(choice == 2):
                russian_roulette()
                condition = False
            else:
                print("Press 1 or 2, and after that enter to play games")
    else:
        print("Critical error")
    print(balance)
main()