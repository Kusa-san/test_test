class Inventory:
    # Class property
    inventory_space = 0

    # Constructor
    def __init__(self):
        self.items = {} # this will store each item with its quantity as follows: { "canned tomato paste": 10, "Dakwa": 39 }

    # Instance Methods
    def add_item(self, item, quantity):
        new_item = 1
        for i in self.items:
            if item == i:
                self.items[i] += quantity
                new_item = 0
        if new_item == 1:
            self.items[item] = quantity
        Inventory.inventory_space += quantity

    def check_stock(self, item):
        print(f"{item}: {self.items.get(item, 0)}")

    @classmethod
    def merge_inventories(cls, first_inventory, second_inventory):
        merged = cls()
        for item in first_inventory.items:
            merged.add_item(item, first_inventory.items[item])
        for item in second_inventory.items:
            merged.add_item(item, second_inventory.items[item])
        return merged

    @staticmethod
    def is_valid_quantity(quantity):
        return isinstance(quantity, int) and quantity >= 0
    
    def __str__(self):
        return f"{self.items}"

# Example Usage:
x = Inventory()
y = Inventory()
x.add_item("Toys", 5)
x.add_item("Knife", 10)

y.check_stock("Hair Brush")
print(Inventory.merge_inventories(x,y))