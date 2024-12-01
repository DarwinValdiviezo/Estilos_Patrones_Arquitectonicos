class Order:
    def __init__(self):
        self.products = []
        self.shipping = 0

    def add_product(self, product):
        self.products.append(product)

    def set_shipping(self, cost):
        self.shipping = cost

    def details(self):
        details = [f"Product: {p.description()}, Cost: {p.cost()}" for p in self.products]
        details.append(f"Shipping: {self.shipping}")
        details.append(f"Total: {sum(p.cost() for p in self.products) + self.shipping}")
        return "\n".join(details)

class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_product(self, product):
        self.order.add_product(product)

    def set_shipping(self, cost):
        self.order.set_shipping(cost)

    def build(self):
        return self.order
