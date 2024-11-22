from models.Product import Product
from typing import Dict

class Order:
    id_general: int = 0
    def __init__(self):
        self.order_products: dict[Product, int] = {}
        self.total_order: float = 0.0
        self.value_tip: float = 0.0
        self.status = False

        self.id_order: int = self.id_general
        self.id_general+=1


    def add_product(self,name: str , quantity: int) ->None:
        ...

    def calculate_total(self) ->None:
        ...

    def check_tip(self,tip:bool):
        if tip:
            self.value_tip = 0.10
            return
        else:
            return