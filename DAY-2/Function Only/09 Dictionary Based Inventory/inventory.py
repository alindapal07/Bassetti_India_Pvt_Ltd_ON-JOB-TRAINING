inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 25
}

class ProductNotFoundError(Exception):
    pass

class InvalidStockError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

def add_product(product, quantity):
    if quantity < 0:
        raise InvalidStockError("Stock cannot be negative")
    if product in inventory:
        raise ValueError("Product already exists")
    inventory[product] = quantity
    return "Product added successfully"

def remove_product(product):
    if product not in inventory:
        raise ProductNotFoundError("Product does not exist")
    del inventory[product]
    return "Product removed successfully"

def sell_product(product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Cannot sell nonexistent product")
    if quantity <= 0:
        raise InvalidStockError("Quantity must be positive")
    if quantity > inventory[product]:
        raise InsufficientStockError("Cannot sell more than available stock")
    inventory[product] -= quantity
    return "Product sold successfully"

def restock_product(product, quantity):
    if product not in inventory:
        raise ProductNotFoundError("Cannot restock nonexistent product")
    if quantity <= 0:
        raise InvalidStockError("Restock quantity must be positive")
    inventory[product] += quantity
    return "Product restocked successfully"

def check_stock(product):
    if product not in inventory:
        raise ProductNotFoundError("Product does not exist")
    return inventory[product]