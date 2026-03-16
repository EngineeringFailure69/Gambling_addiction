import random

def chance_for_the_item_to_break():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    if first_number == second_number:
        return True
    else:
        return False
    