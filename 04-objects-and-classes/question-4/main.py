class Restaurant:
    """A class to manage restaurant operations including menu, table reservations, and customer orders."""
    
    def __init__(self):
        self.menu_items = []
        self.table_reservations = []
        self.customer_orders = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)
        print(f"Added '{item}' to the menu.")

    def book_table(self, table_number):
        self.table_reservations.append(table_number)
        print(f"Table {table_number} has been reserved.")

    def take_customer_order(self, order):
        self.customer_orders.append(order)
        print(f"Order taken: {order}")

    def print_menu(self):
        print("Menu Items:")
        for item in self.menu_items:
            print(f"- {item}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table in self.table_reservations:
            print(f"- Table {table}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"- {order}")

def main():
    restaurant = Restaurant()
    
    while True:
        print("\n1. Add Item to Menu")
        print("2. Book Table")
        print("3. Take Customer Order")
        print("4. Print Menu")
        print("5. Print Table Reservations")
        print("6. Print Customer Orders")
        print("7. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            item = input("Enter menu item: ")
            restaurant.add_item_to_menu(item)
        elif choice == 2:
            table_number = input("Enter table number: ")
            restaurant.book_table(table_number)
        elif choice == 3:
            order = input("Enter customer order: ")
            restaurant.take_customer_order(order)
        elif choice == 4:
            restaurant.print_menu()
        elif choice == 5:
            restaurant.print_table_reservations()
        elif choice == 6:
            restaurant.print_customer_orders()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
