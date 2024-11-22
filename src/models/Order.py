from Inventory import Inventory
from models.Product import Product
from typing import Dict


class Order:
    id_general: int = 0
    def __init__(self):
        self.order_products: dict[Product:int] = {}
        self.total_order: float = 0.0
        self.value_tip: float = 0.0
        self.status = False

        self.id_order: int = self.id_general
        self.id_general += 1

    def add_product(self, name: str , quantity: int, inventory: Inventory) -> None:
        result =  inventory.update_quantity_product(name, quantity, False)
        if result:
            if result not in self.order_products:
                self.order_products[result] = quantity
            else:
                self.order_products[result] += quantity

    def calculate_total(self) -> None:
        count = 0
        for product, quantity in self.order_products.items():
            count += product.price * quantity
        self.total_order = count
        return

    def check_tip(self, tip: bool):
        if tip:
            self.value_tip = self.total_order * 0.10
            return
        else:
            return
