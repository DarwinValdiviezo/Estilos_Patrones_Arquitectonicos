class BaseProduct:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def description(self):
        return self._name

    def cost(self):
        return self._cost

class ExtraWarranty:
    def __init__(self, product):
        self._product = product

    def description(self):
        return self._product.description() + " with Extra Warranty"

    def cost(self):
        return self._product.cost() + 50

class GiftWrap:
    def __init__(self, product):
        self._product = product

    def description(self):
        return self._product.description() + " with Gift Wrap"

    def cost(self):
        return self._product.cost() + 10
