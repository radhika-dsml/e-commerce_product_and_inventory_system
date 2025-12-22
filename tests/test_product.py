import pytest
from .src.models.Product import product

class TestProduct:
    def test_product_creation(self):
        product = Product("Laptop", "P001", 1000.0, "High-end gaming laptop", "BrandA")
        assert product.name == "Laptop"
        assert product.ID == "P001"
        assert product.price == 1000.0
        assert product.description == "High-end gaming laptop"
        assert product.brand == "BrandA"