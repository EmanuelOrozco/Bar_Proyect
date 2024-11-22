from models.Product import Product
from typing import Dict

class Inventory:
    inventory: Dict[Product, int]

    def __init__(self):
        self.inventory = {}

    def update_quantity_product(self, product: Product, quantity: int, check: bool)->None:
        if product not in self.inventory:
            self.inventory[product] = 0

        if check: 
            self.inventory[product] += quantity
        else:
            if self.inventory[product] - quantity < 0 :
                print("there are not enough products in inventory")
            else:
                self.inventory[product]-= quantity

    def add_product(self, name_product: str, quantity: int) -> None:
        for product in self.inventory.keys():
            if product == name_product:
                self.inventory[product] += quantity
                return

        new_product = Product(name = name_product)
        self.inventory[new_product] = quantity
