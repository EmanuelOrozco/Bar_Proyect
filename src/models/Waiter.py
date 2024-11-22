from models.Order import Order
from typing import List


class Waiter:
    id_general: int = 1

    def __init__(self, name: str, password: str):
        self.password: str = password
        self.name: str = name

        self.orders_placed: List[Order] = []
        self.total_value_tips: float = 0.0
        self.total_tips: int = 0
        self.total_customers: int = 0
        self.waiter_effectiveness: int = 0

        self.id_waiter: int = self.id_general
        self.id_general += 1

    def update_waiter():
        ...
    
    def generate_order():
        ...
    
    def pay_order():
        ...
