# Create a class ShoppingCart:
class ShoppingCart:
    # Initialize constructor to provide class attribute:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020", cart_items = {}):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # define a function to add an item to the cart:
    def add_item(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.cart_items[item_name] = [item_price, item_quantity, item_description]

    # define a function to remove an item from the cart:
    def remove_item(self, item_name):
        if item_name in self.cart_items.keys():
            del self.cart_items[item_name]
            print(f"Item {item_name} has been removed from the cart.")
        else:
            print("Item not found in cart.")

    #define a function to change the quantity of an item in the cart:
    def modify_item(self, item_name, item_quantity):
        self.cart_items[item_name][1] = item_quantity

    #define a function to get the total number of items in the cart:
    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for i in self.cart_items.keys():
            num_items_in_cart += self.cart_items[i][1]
        return num_items_in_cart
    
    #define a function to get the total cost of the cart:
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items.keys():
            total += self.cart_items[item][0] * self.cart_items[item][1]
        return total

    #define a function to print the customer's name and the date:
    def print_customer_name(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

    #define a function to print the total cost of the cart:
    def print_total(self):
        self.print_customer_name()
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for i, j in self.cart_items.items():
                print(f"{i} {j[1]:,} @ ${j[0]:,.2f} = ${j[1]*j[0]:,.2f}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print(f"TOTAL COST: ${self.get_cost_of_cart():,.2f}")

    #define a function to print the description of each item in the cart:
    def print_description(self):
        self.print_customer_name()
        print("Item Description")
        for i,j in self.cart_items.items():
            print(f"{i}: {j[2]}")

#define a function to print the menu:
def print_menu():
    name = input("Enter your name: ")
    date = input("Enter today's date: ")
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("Choose an option: ", end = "")
    options = input().lower()
    cart = ShoppingCart(name, date)
    while True:
        if options == "a":
            name = input("Enter the name of the item: ")
            if name not in cart.cart_items.keys():
                price = float(input("Enter the price of the item: "))
                quantity = int(input("Enter the quantity of the item: "))
                description = input("Enter the description of the item: ")
                cart.add_item(name, price, quantity, description)
            else:
                print("Item already exists.")
        elif options == "r":
            remove_item = input("Enter the name of the item to remove: ")
            cart.remove_item(remove_item)
        elif options == "c":
            change_item = input("Enter the name of the item to change: ")
            if change_item in cart.cart_items.keys():
                change_quantity = int(input("Enter the new quantity of the item: "))
                cart.modify_item(change_item, change_quantity)
            else:
                print("Item not found in cart.")
        elif options == "i":
            cart.print_description()
        elif options == "o":
            cart.print_total()
        elif options == "q":
            print("Thank you for shopping with us!")
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option: ", end = "")
        options = input().lower()
print_menu()

