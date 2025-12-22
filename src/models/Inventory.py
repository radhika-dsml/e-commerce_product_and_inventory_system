class Inventory:
    def __init__(self):
        self.products = {}  # key: product ID, value: quantity

    def add_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity

    def remove_product(self, product_id, quantity):
        if product_id in self.products:
            if self.products[product_id] >= quantity:
                self.products[product_id] -= quantity
                if self.products[product_id] == 0:
                    del self.products[product_id]
            else:
                raise ValueError("Not enough stock to remove")
        else:
            raise KeyError("Product not found in inventory")

    def check_stock(self, product_id):
        return self.products.get(product_id, 0)
    
    def track_low_stock(self, threshold):
        low_stock_items = {pid: qty for pid, qty in self.products.items() if qty <= threshold}
        return low_stock_items
    
    def availability_report(self):
        return self.products
