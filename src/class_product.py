class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price,quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
