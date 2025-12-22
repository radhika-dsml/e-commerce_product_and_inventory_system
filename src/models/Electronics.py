from .Product import Product
class Electronics(Product):
    def __init__(self, name, ID, price, description, brand, warranty_period, power_consumption):
        super().__init__(name, ID, price, description, brand)
        self.warranty_period = warranty_period
        self.power_consumption = power_consumption

