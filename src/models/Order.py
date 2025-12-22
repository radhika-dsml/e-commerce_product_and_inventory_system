import uuid
from datetime import datetime
class Order:
    def __init__(self, order_id, user, products, total_amount, status):
        self.order_id = self.generate_order_id()
        self.user = user  # Instance of User class
        self.products = products  # List of Product instances
        self.total_amount = total_amount
        self.status = status  # e.g., 'Pending', 'Shipped', 'Delivered' 

    def generate_order_id(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id= str(uuid.uuid4())[:8]
        return f"ORD-{timestamp}-{unique_id}"
    
    def convert_cart_to_order(self, cart):
        self.products = [item["product"] for item in cart.items]
        self.total_amount = cart.calculate_total()
        self.status = 'Pending'

    def order_status_update(self, new_status):
        self.status = new_status

    def tax_and_discount_calculation(self, tax_rate,discount_rate):
        tax_amount = self.total_amount * tax_rate
        discount_amount = self.total_amount * discount_rate
        self.total_amount = self.total_amount + tax_amount - discount_amount
        return self.total_amount

    def shipping_address_management(self, new_address):
        self.user.address = new_address
           
    
