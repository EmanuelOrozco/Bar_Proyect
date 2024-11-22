from models.Order import Order
from typing import List


class Table:
    id_general: int = 0
    def __init__(self):
        self.orders_placed: list[Order] = []
        self.total_table = 0.0

        self.id_table = self.id_general
        self.id_general+= 1

    def calculate_total_table(self) -> None:
       for order in self.orders_placed:
           self.total_table += order.total_order
