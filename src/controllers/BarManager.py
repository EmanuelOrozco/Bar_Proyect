from models.Waiter import Waiter
from models.Table import Table


class BarManager:

    def show_tables(self):
        ...

    def show_waiter(self):
        ...

    def show_total_effectiveness_per_waiter(self, waiter: Waiter):
        return waiter.waiter_effectiveness
    
    def show_total_customer_per_Waiter(self, waiter: Waiter):
        return waiter.total_customers

    def show_total_tip_per_waiter(self, waiter: Waiter):
        return waiter.total_value_tips

    def update_waiter(self, waiter: Waiter):
        waiter.update_waiter()

    def generate_order(self, table_id: int, waiter: Waiter):
        waiter.generate_order(table_id)

    def finish_order(self,table: Table, waiter: Waiter):
        waiter.finish_order(table)
