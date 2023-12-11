import json

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, product_name, price, quantity, threshold=10):
        if product_id not in self.inventory:
            self.inventory[product_id] = {'name': product_name, 'price': price, 'quantity': quantity, 'threshold': threshold, 'sales': 0}
            print(f"Product added to inventory: {product_name}")
        else:
            print(f"Product with ID {product_id} already exists in inventory.")

    def remove_product(self, product_id):
        if product_id in self.inventory:
            removed_product = self.inventory.pop(product_id)
            print(f"Product removed from inventory: {removed_product['name']}")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def update_product_details(self, product_id, new_name=None, new_price=None, new_quantity=None, new_threshold=None):
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if new_name:
                product['name'] = new_name
            if new_price:
                product['price'] = new_price
            if new_quantity is not None:
                product['quantity'] = new_quantity
            if new_threshold is not None:
                product['threshold'] = new_threshold
            print(f"Product details updated for {product['name']}")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def display_current_inventory(self):
        print("Current Inventory:")
        for product_id, product_info in self.inventory.items():
            print(f"ID: {product_id}, Name: {product_info['name']}, Price: ${product_info['price']:.2f}, Quantity: {product_info['quantity']}")

    def track_stock_levels(self):
        print("Low Stock Alert:")
        for product_id, product_info in self.inventory.items():
            if product_info['quantity'] < product_info['threshold']:
                print(f"Low stock alert for {product_info['name']}. Current quantity: {product_info['quantity']}")

    def generate_purchase_orders(self):
        print("Purchase Orders:")
        for product_id, product_info in self.inventory.items():
            if product_info['quantity'] < product_info['threshold']:
                order_quantity = product_info['threshold'] - product_info['quantity'] + 10  # Order 10 more to avoid frequent orders
                print(f"Generate purchase order for {order_quantity} units of {product_info['name']} (ID: {product_id})")

    def calculate_total_inventory_value(self):
        total_value = sum(product_info['price'] * product_info['quantity'] for product_info in self.inventory.values())
        print(f"Total Inventory Value: ${total_value:.2f}")

    def set_low_stock_alert(self, product_id, new_threshold):
        if product_id in self.inventory:
            self.inventory[product_id]['threshold'] = new_threshold
            print(f"Low stock alert threshold updated for product {self.inventory[product_id]['name']}")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def record_product_sale(self, product_id, quantity_sold):
        if product_id in self.inventory:
            product_info = self.inventory[product_id]
            if quantity_sold <= product_info['quantity']:
                product_info['quantity'] -= quantity_sold
                product_info['sales'] += quantity_sold
                print(f"Sale recorded for {quantity_sold} units of {product_info['name']}. Updated quantity: {product_info['quantity']}")
            else:
                print(f"Insufficient stock for sale. Available quantity: {product_info['quantity']}")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def export_inventory_data(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.inventory, file)
        print(f"Inventory data exported to file: {file_path}")

# Example Usage:
# Initialize the InventoryManagementSystem
inventory_system = InventoryManagementSystem()

# Add products
inventory_system.add_product("P001", "Laptop", 999.99, 50)
inventory_system.add_product("P002", "Mouse", 19.99, 100, threshold=20)

# Update product details
inventory_system.update_product_details("P001", new_quantity=40)
inventory_system.update_product_details("P002", new_threshold=15)

# Display current inventory
inventory_system.display_current_inventory()

# Track stock levels
inventory_system.track_stock_levels()

# Generate purchase orders
inventory_system.generate_purchase_orders()

# Calculate total inventory value
inventory_system.calculate_total_inventory_value()

# Set low stock alert threshold
inventory_system.set_low_stock_alert("P001", new_threshold=10)

# Record product sale
inventory_system.record_product_sale("P001", quantity_sold=5)

# Export inventory data to a file
inventory_system.export_inventory_data("inventory_data.json")
