class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "laptop":
            return Product("Laptop", 1000)
        elif product_type == "phone":
            return Product("Phone", 500)
        else:
            raise ValueError("Unknown product type")
