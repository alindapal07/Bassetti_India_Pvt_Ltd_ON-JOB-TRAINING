# Inventory Main Program
# Dictionary-Based Inventory
#
# Create:
#
# inventory = {
#     "laptop": 10,
#     "mouse": 50,
#     "keyboard": 25
# }
#
# Implement:
#
# 1. add_product()
# 2. remove_product()
# 3. sell_product()
# 4. restock_product()
# 5. check_stock()
#
# Rules:
#
# - Product cannot have negative stock.
# - Cannot sell more than available stock.
# - Cannot restock a nonexistent product.
# - Cannot sell a nonexistent product.




from inventory import (
    inventory,
    add_product,
    remove_product,
    sell_product,
    restock_product,
    check_stock,
    ProductNotFoundError,
    InvalidStockError,
    InsufficientStockError
)

try:
    print("Initial Inventory:", inventory)

    print(add_product("monitor", 15))
    print(sell_product("laptop", 3))
    print(restock_product("mouse", 20))
    print("Laptop stock:", check_stock("laptop"))
    print(remove_product("keyboard"))

    print("Final Inventory:", inventory)

except ProductNotFoundError as e:
    print("Product Error:", e)
except InvalidStockError as e:
    print("Stock Error:", e)
except InsufficientStockError as e:
    print("Stock Error:", e)
except ValueError as e:
    print("Error:", e)