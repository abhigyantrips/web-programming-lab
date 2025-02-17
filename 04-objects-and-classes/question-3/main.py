class Inventory:
    """Manage inventory items with details like item_id, item_name, stock_count, and price."""
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
        print(f"Item {item_name} added successfully.")
    
    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Item {item_id} updated successfully.")
        else:
            print("Item not found.")
    
    def check_item_details(self, item_id):
        item = self.items.get(item_id)
        if item:
            print(f"Details for {item_id}: {item}")
        else:
            print("Item not found.")

def main():
    inventory = Inventory()
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Check Item Details")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            item_id = input("Enter item ID: ")
            item_name = input("Enter item name: ")
            stock_count = int(input("Enter stock count: "))
            price = float(input("Enter price: "))
            inventory.add_item(item_id, item_name, stock_count, price)
        
        elif choice == '2':
            item_id = input("Enter item ID to update: ")
            stock_count = input("Enter new stock count (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            inventory.update_item(item_id, 
                                  stock_count=int(stock_count) if stock_count else None, 
                                  price=float(price) if price else None)
        
        elif choice == '3':
            item_id = input("Enter item ID to check: ")
            inventory.check_item_details(item_id)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
