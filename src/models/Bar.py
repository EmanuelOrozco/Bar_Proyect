from Table import Table
from Waiter import Waiter
from Admin import Admin
from Inventory import Inventory


class Bar:
    def __init__(self):
        self.tables: list[Table] = []
        self.waiters: list[Waiter] = []
        self.admins: list[Admin] = []
        self.inventory: Inventory
        total_tables: float = 0.0

    def show_tables(self):
        ...

    def show_waiter(self):
        ...
    
    def show_total_effectiveness_per_waiter(self, id_waiter: int):
        for waiter in self.waiters:
            if waiter.id_Waiter == id_waiter:
                return waiter.waiter_effectiveness
    
    def show_total_customer_per_Waiter(self, id_waiter: int):
        for waiter in self.waiters:
            if waiter.id_waiter == id_waiter:
                return waiter.total_customers
    
    def show_total_tip_per_waiter(self, id_waiter: int):
        for waiter in self.waiters:
            if waiter.id_waiter == id_waiter:
                return waiter.total_tips
