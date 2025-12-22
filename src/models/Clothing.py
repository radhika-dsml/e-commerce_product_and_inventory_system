from .Product import Product
from .Interfaces import DiscountableInterface, TaxableInterface
class Clothing(Product):
    def __init__(self, name, ID, price, description, brand, size, material, gender,season):
        super().__init__(name, ID, price, description, brand)
        self.size = size
        self.material = material
        self.gender=gender
        self.season=season

    def apply_discount(self):
        percent = 10 if self.season.lower() == 'winter' else 15
        discount_amount = self.price * (percent / 100) #5 percent standard discount for category electronics
        self.price -= discount_amount
        return self.price           
        
    def calculate_tax(self):
        tax_amount = self.price * (12/100)
        return tax_amount

    def calculate_final_price(self, tax_rate):
        tax_amount = self.calculate_tax(tax_rate)
        discounted_amount = self.apply_discount(10)
        final_price = self.price -discounted_amount+ tax_amount
        return final_price