from models.Inventory import Inventory
from models.Order import Order
from models.Waiter import Waiter


class OrderManager:
    def add_product_inventory(self, name_product: str, price: float, quantity: int, inventory: Inventory) -> None:
        inventory.add_product_inventory(name_product, price, quantity)
    
    def update_quantity_product(self, name: str, quanity: int, check: bool, inventory: Inventory):
        inventory.update_quantity_product(name, quanity, check)
    
    def add_product(self, name: str, quantity: int, inventory: Inventory, order: Order) -> None:
        order.add_product(name, quantity, inventory)
    
    def calculate_total(self, order: Order) -> None:
        order.calculate_total()
    
    def check_tip(self, tip: bool, order: Order):
        order.check_tip(tip)
    
    def generate_order(self, waiter: Waiter, table_id: int):
        waiter.generate_order(table_id)
