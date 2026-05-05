# ===== FOOD ORDERING APP (EASY VERSION) =====

# Menu (simple)
menu = {
    "pizza": {"price": 10},
    "burger": {"price": 8},
    "biryani": {"price": 12},
    "samosa": {"price": 3},
    "chai": {"price": 2},
    "juice": {"price": 4},
    "chicken": {"price": 9},
    "naan": {"price": 2}
}

# Cart
cart = {}


# 1. Show Menu
def show_menu():
    print("\n--- MENU ---")
    for item in menu:
        print(item, "=", menu[item]["price"])


# 2. Add to Cart
def add_item(item, qty):
    if item not in menu:
        print("Item not found!")
        return

    if qty <= 0:
        print("Enter valid quantity!")
        return

    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    print("Item added!")


# 3. Show Cart
def show_cart():
    if not cart:
        print("Cart is empty")
        return

    print("\n--- YOUR CART ---")

    total = 0
    for item in cart:
        qty = cart[item]
        price = menu[item]["price"]
        item_total = qty * price

        print(item, "x", qty, "=", item_total)
        total += item_total

    print("Subtotal =", total)

    tax = total * 0.10
    print("Tax =", tax)

    final = total + tax
    print("Total =", final)


# 4. Update Quantity
def update_item(item, qty):
    if item not in cart:
        print("Item not in cart")
        return

    if qty <= 0:
        print("Invalid quantity")
        return

    cart[item] = qty
    print("Quantity updated")


# 5. Remove Item
def remove_item(item):
    if item in cart:
        del cart[item]
        print("Item removed")
    else:
        print("Item not in cart")


# 6. Clear Cart
def clear_cart():
    if not cart:
        print("Cart already empty")
        return

    cart.clear()
    print("Cart cleared")


# 7. Place Order
def place_order():
    if not cart:
        print("Cart is empty")
        return

    show_cart()

    choice = input("Confirm order? (yes/no): ").lower()

    if choice == "yes":
        print("Order placed!")
        cart.clear()
    else:
        print("Order cancelled")


# ===== MAIN PROGRAM =====
def main():
    while True:
        print("\n--- FOOD APP ---")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. Show Cart")
        print("4. Update Quantity")
        print("5. Remove Item")
        print("6. Clear Cart")
        print("7. Place Order")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            show_menu()
            item = input("Enter item name: ").lower()
            try:
                qty = int(input("Enter quantity: "))
                add_item(item, qty)
            except:
                print("Enter number only!")

        elif choice == "3":
            show_cart()

        elif choice == "4":
            item = input("Enter item name: ").lower()
            try:
                qty = int(input("New quantity: "))
                update_item(item, qty)
            except:
                print("Enter number only!")

        elif choice == "5":
            item = input("Enter item name: ").lower()
            remove_item(item)

        elif choice == "6":
            clear_cart()

        elif choice == "7":
            place_order()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Wrong choice")


# Run
main()