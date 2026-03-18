import random
import const
import utils.draw_functions as draw_functions
import tkinter.messagebox as dialog_box

def chance_for_the_item_to_break():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    if first_number == second_number:
        return True

def repair_car(repair, repair_price):
    repaired = ""
    if repair:
        if const.balance >= repair_price:
            const.balance = const.balance - repair_price
            draw_functions.draw_message_box("Item repaired", "Your car was repaired and it works again")
            repaired = "repaired"
            return repaired
        else:
            draw_functions.draw_message_box("No money", "You don't have enough money to repair your car, and now it will be discarded")
            repaired = "not repaired"
            return repaired
    else:
        repaired = "not repaired"
        return repaired

def car_break_crash_death(car):
    repaired = True
    car_is_broken = chance_for_the_item_to_break()
    if car_is_broken:
        repair = dialog_box.askyesno("Oh no, your car broke down!", f"Your car broke down, you can fix it by paying {car.item_price / 2}, or discard it")
        repair_price = car.item_price / 2
        repaired = repair_car(repair, repair_price)
        return repaired
    elif not car_is_broken:
        car_crash_1 = random.randint(1, 10)
        car_crash_2 = random.randint(1, 10)
        if car_crash_1 == car_crash_2:
            death_chance_1 = random.randint(1, 10)
            death_chance_2 = random.randint(1, 10)
            if death_chance_1 == death_chance_2:
                return "dead"
            else:
                repair_price = car.item_price * 0.8
                repair = dialog_box.askyesno("Oh no, you crashed your car!", f"You crashed your car, you can fix it by paying {car.item_price * 0.8}, or discard it")
                repaired = repair_car(repair, repair_price)
                return repaired
