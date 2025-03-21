class BillSystem:
    def __init__(self):
        self.items = [
            {"id": 1, "name": "Ice-cream", "price": 50.00},
            {"id": 2, "name": "Biscuits", "price": 60.00},
            {"id": 3, "name": "Milk Drink", "price": 120.00},
            {"id": 4, "name": "Chocolate", "price": 100.00},
            {"id": 5, "name": "Chunky Choc", "price": 160.00}
        ]
        self.selected_items = []

    def show_items(self):
        print("\nAvailable Items:")
        for item in self.items:
            print(f"{item['id']}. {item['name']} - Rs.{item['price']:.2f}")

    def select_items(self):
        while True:
            self.show_items()
            try:
                item_id = int(input("\nEnter item number to add (or 0 to finish): "))
                if item_id == 0:
                    break
                
                item = next((i for i in self.items if i["id"] == item_id), None)
                if item:
                    quantity = int(input(f"Enter quantity for {item['name']}: "))
                    self.selected_items.append({"name": item["name"], "price": item["price"], "quantity": quantity})
                else:
                    print("Invalid item number! Try again.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

    def calculate_total(self):
        return sum(item["price"] * item["quantity"] for item in self.selected_items)

    def print_bill(self):
        print("\n<< --- BILL INVOICE --- >>")
        for item in self.selected_items:
            print(f"{item['name']} x {item['quantity']} - ${item['price'] * item['quantity']:.2f}")
        print(f"\nTotal: ${self.calculate_total():.2f}")
        print("--------------------\n")

# Example Usage
bill = BillSystem()
bill.select_items()
bill.print_bill()
