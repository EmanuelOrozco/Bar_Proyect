from models.Product import Product
from typing import Dict

class Inventory:
    inventory: Dict[Product, int]

    def __init__(self):
        self.inventory = {}

    def update_quantity_product(self, product: Product, quantity: int, check: bool):
        if product not in self.inventory:
            self.inventory[product] = 0  

        if check: 
            self.inventory[product] += quantity
        else: 
            ...