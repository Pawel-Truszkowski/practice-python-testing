import pytest
from cart import Cart


@pytest.fixture
def products():
    return [
        {"name": "apple", "price": 3.5},
        {"name": "banana", "price": 3.5},
        {"name": "apple", "price": 4.2}
    ]
    
def test_items_return_all_products(products):
    cart = Cart()
    for product in products: cart.add(product)
    assert cart.items() == products

def test_add_product(products):
    cart = Cart()
    cart.add(products[0])
    assert cart.items() == [{"name": "apple", "price": 3.5}]
    cart.add(products[1])
    assert cart._products == [{"name": "apple", "price": 3.5}, {"name": "banana", "price": 3.5}]
    


def test_remove_product(products):
    cart = Cart()
    for product in products: cart.add(product)
    result = cart.remove("apple")
    assert cart.items() == [
        {"name": "banana", "price": 3.5},
        {"name": "apple", "price": 4.2}
    ]
    assert result == True


def test_total_price(products):
    cart = Cart()
    for product in products: cart.add(product)
    assert cart.total() == 11.2
 
    
def test_empty_cart_total():
    cart = Cart()
    assert cart.total() == 0


def test_remove_nonexistent_product(products):
    cart = Cart()
    for product in products: cart.add(product)
    result = cart.remove("nonexistent")
    assert cart.items() == products
    assert result == False
    