from Table import Table
from Order import Order
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
        self.current_order = None

    def update_waiter(self):
        self.total_value_tips = 0
        self.total_tips = 0

        for order in self.orders_placed:
            self.total_value_tips += order.value_tip
            if order.value_tip != 0:
                self.total_tips += 1
        self.total_customers += 1
        self.waiter_effectiveness = (self.total_tips/self.total_customers)
        return 
    
    def generate_order(self, table_id: int) -> None:
        new_order = Order()
        new_order.waiter_id = self.id_waiter
        new_order.table_id = table_id
        self.current_order = new_order
        return

    def pay_order(self, table: Table) -> None:
        self.current_order.status = True
        self.orders_placed.append(self.current_order)
        table.orders_placed.append(self.current_order)
        self.update_waiter()
        return