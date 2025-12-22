class Cart:
    def __init__(self, user):
        self.user = user  # Instance of User class
        self.items = []  # List to hold products added to the cart

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        self.items = [item for item in self.items if item["product"] != product]

    def update_item(self, product, quantity):
        for item in self.items:
            if item["product"] == product:
                item["quantity"] = quantity
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def clear_cart(self):
        self.items = [] 

    def view_cart_with_details(self):
        cart_details = []
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            cart_details.append({
                "product_name": product.name,
                "product_id": product.ID,
                "price_per_unit": product.price,
                "quantity": quantity,
                "total_price": product.price * quantity
            })
        return cart_details