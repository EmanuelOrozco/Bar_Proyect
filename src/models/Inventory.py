from models.Product import Product
from typing import Dict


class Inventory:
    inventory: Dict[Product, int]

    def __init__(self):
        self.inventory = {}

    def update_quantity_product(self, name_product: str, quantity: int, check: bool) -> bool:
        for product in self.inventory:
            if product.name == name_product.lower():
                if check:
                    self.inventory[product] += quantity
                else:
                    if self.inventory[product] - quantity < 0 :
                        print("Not enough product in the inventory")
                        return product
                    else:
                        self.inventory[product] -= quantity
                        return True

    def add_product(self, name_product: str, price: float, quantity: int) -> None:
        new_product = Product(name_product, price)
        self.inventory[new_product] = quantity
        return
