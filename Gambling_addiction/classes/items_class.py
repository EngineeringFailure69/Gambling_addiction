class shop_item:
    def __init__(self, type, image_path, item_type, item_price, item_tax = 0):
        self.type = type
        self.image_path = image_path
        self.item_type = item_type
        self.item_price = item_price
        self.item_tax = item_tax

class apartment:
    def __init__(self, index, price, rent_price, image_path, renting_apartment, bought_apartment, renting_expenses, bought_expenses):
        self.index = index
        self.price  = price
        self.rent_price =  rent_price
        self.image_path = image_path
        self.renting_apartment = renting_apartment
        self.bought_apartment = bought_apartment
        self.renting_expenses = renting_expenses
        self.bought_expenses = bought_expenses