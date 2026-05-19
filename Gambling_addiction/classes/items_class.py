class shop_item:
    def __init__(self, type, image_path, item_type,  item_price):
        self.type = type
        self.image_path = image_path
        self.item_type = item_type
        self.item_price = item_price

class apartment:
    def __init__(self, price, rent_price, image_path):
        self.price  = price
        self.rent_price =  rent_price
        self.image_path = image_path