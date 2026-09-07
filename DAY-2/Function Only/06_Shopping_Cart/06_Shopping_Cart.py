# Shopping Cart
#
# Represent products as:
#
# products = [
#     {"id": 1, "name": "Laptop", "price": 70000},
#     {"id": 2, "name": "Mouse", "price": 1200},
#     {"id": 3, "name": "Keyboard", "price": 2500}
# ]
#
# Implement:
#
# 1. add_to_cart()
# 2. remove_from_cart()
# 3. calculate_subtotal()
# 4. calculate_discount()
# 5. calculate_tax()
# 6. calculate_final_amount()
#
# Rules:
#
# - Product must exist.
# - Quantity must be positive.
# - Cannot remove something that isn't in the cart.
# - Discount depends on total amount.
#
# Error Handling:
#
# - Use exceptions for invalid cases.




# Shopping Cart

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 1200},
    {"id": 3, "name": "Keyboard", "price": 2500}
]
cart = []
# Add product to cart
def add_to_cart(product_id, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    for product in products:
        if product["id"] == product_id:
            item = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            }
            cart.append(item)
            return "Product added to cart"
    raise ValueError("Product does not exist")


# Remove product from cart
def remove_from_cart(product_id):
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            return "Product removed from cart"
    raise ValueError("Product is not present in cart")


# Calculate subtotal
def calculate_subtotal():
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal

# Calculate discount
def calculate_discount(subtotal):
    if subtotal >= 50000:
        return subtotal * 0.10

    elif subtotal >= 20000:
        return subtotal * 0.05
    else:
        return 0

# Calculate tax
def calculate_tax(amount):
    return amount * 0.18


# Calculate final amount
def calculate_final_amount():
    subtotal = calculate_subtotal()
    discount = calculate_discount(subtotal)
    amount_after_discount = subtotal - discount
    tax = calculate_tax(amount_after_discount)
    final_amount = amount_after_discount + tax
    return final_amount


# Main Program
try:
    add_to_cart(1, 1)
    add_to_cart(2, 2)
    add_to_cart(3, 1)

    print("Cart:", cart)
    subtotal = calculate_subtotal()
    discount = calculate_discount(subtotal)

    tax = calculate_tax(subtotal - discount)
    final_amount = calculate_final_amount()

    print("\n----- BILL -----")
    print("Subtotal :", subtotal)
    print("Discount :", discount)
    print("Tax      :", tax)
    print("Final Amount :", final_amount)


except ValueError as e:

    print("Error:", e)