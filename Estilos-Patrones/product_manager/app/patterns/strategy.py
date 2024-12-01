class ShippingStrategy:
    def calculate(self, weight):
        raise NotImplementedError

class StandardShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 5

class ExpressShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 10

class FreeShipping(ShippingStrategy):
    def calculate(self, weight):
        return 0
