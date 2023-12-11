import unittest
import json
import os

from main import InventoryManagementSystem


class TestInventoryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.inventory_system = InventoryManagementSystem()

    def test_add_product(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 50)
        self.assertEqual(len(self.inventory_system.inventory), 1)

    def test_remove_product(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 50)
        self.inventory_system.remove_product("P001")
        self.assertEqual(len(self.inventory_system.inventory), 0)

    def test_update_product_details(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 50)
        self.inventory_system.update_product_details("P001", new_quantity=40)
        self.assertEqual(self.inventory_system.inventory["P001"]["quantity"], 40)

    def test_display_current_inventory(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 50)
        self.assertEqual(self.inventory_system.display_current_inventory(), "Current Inventory:\nID: P001, Name: Laptop, Price: $999.99, Quantity: 50")

    def test_track_stock_levels(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 5, threshold=10)
        self.assertEqual(self.inventory_system.track_stock_levels(), "Low Stock Alert:\nLow stock alert for Laptop. Current quantity: 5")

    def test_generate_purchase_orders(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 5, threshold=10)
        self.assertEqual(self.inventory_system.generate_purchase_orders(), "Purchase Orders:\nGenerate purchase order for 15 units of Laptop (ID: P001)")

    def test_calculate_total_inventory_value(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 5)
        self.assertEqual(self.inventory_system.calculate_total_inventory_value(), "Total Inventory Value: $4999.95")

    def test_set_low_stock_alert(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 5, threshold=10)
        self.inventory_system.set_low_stock_alert("P001", new_threshold=8)
        self.assertEqual(self.inventory_system.inventory["P001"]["threshold"], 8)

    def test_record_product_sale(self):
        self.inventory_system.add_product("P001", "Laptop", 999.99, 10)
        self.inventory_system.record_product_sale("P001", quantity_sold=5)
        self.assertEqual(self.inventory_system.inventory["P001"]["quantity"], 5)


    def tearDown(self):
        # Clean up any created test files
        try:
            with open("test_inventory_data.json", "r"):
                pass
            # Remove the file after the test
            os.remove("test_inventory_data.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
