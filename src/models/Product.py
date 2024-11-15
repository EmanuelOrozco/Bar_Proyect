class Product:
    id_general: int = 0

    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

        self.id_product: int = self.id_general
        self.id_general += 1
