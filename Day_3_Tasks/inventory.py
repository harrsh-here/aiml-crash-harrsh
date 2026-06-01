# Description: Implements a database engine utilizing structured product models bound to an tracking manager.

import csv
from typing import Optional

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def total_value(self) -> float:
        return sum(p.price * p.quantity for p in self.products)

    def find_product(self, name: str) -> Optional[Product]:
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def save_to_csv(self, filename: str) -> None:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'price', 'quantity'])
            for p in self.products:
                writer.writerow([p.name, p.price, p.quantity])

    @classmethod
    def load_from_csv(cls, filename: str) -> 'Inventory':
        # @staticmethod passes no implicit structural references. It acts purely as an isolated function bound to a class scope.
        # @classmethod explicitly passes the class namespace reference (cls), enabling factory setups that instantiate objects directly.
        inv = cls()
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    inv.add_product(Product(row[0], float(row[1]), int(row[2])))
        return inv

if __name__ == "__main__":
    my_inv = Inventory()
    my_inv.add_product(Product("Laptop", 999.99, 5))
    my_inv.add_product(Product("Mouse", 25.50, 20))

    print(my_inv.total_value())
    my_inv.save_to_csv("inventory.csv")

    loaded_inv = Inventory.load_from_csv("inventory.csv")
    found = loaded_inv.find_product("laptop")
    if found:
        print(f"Found: {found.name} | Stock: {found.quantity}")