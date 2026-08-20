**Name:** Shaun Rodric B. Dy
**Section:** 9 - Platinum
**Last Name:** Dy
**Date:** August 20, 2026

# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation protects data from accidental changes, makes code easier to maintain, and lets you safely update internal code without breaking other parts of the program. By making these variables private and exposing controlled public methods like `update_stock()` or `get_price()`, the system ensures that values cannot be set to invalid states, such as negative stock counts. This improves code organization by centralizing data validation within the class itself rather than scattering procedural checks throughout the codebase.

    class Product:
        def __init__(self, name: str, price: float, stock: int):
            self._name = name
            self._price = price
            self._stock = stock

        def reduce_stock(self, quantity: int):
            if 0 < quantity <= self._stock:
                self._stock -= quantity
                return True
            return False

### 2. Abstraction
Abstraction hides complex internal code details and shows only the important features. For example, a store clerk interacts with a high-level ⁠process_sale()⁠ method on an ⁠InventoryManager⁠ object without needing to see the internal array lookups, receipt formatting, or mathematical calculations occurring in the background. Hiding these implementation details reduces cognitive load for developers and makes the overall program easier to maintain and extend over time.

    class InventoryManager:
        def process_sale(self, product_id: str, quantity: int):
            product = self._find_product(product_id)
            if product and product.reduce_stock(quantity):
                self._record_transaction(product, quantity)
    
    class Product:
        def __init__(self, name: str, price: float, stock: int):
            self.name = name
            self.price = price
            self.stock = stock

### 3. Inheritance
  Inheritance automatically receives, modify, and expand upon the attributes and methods of a base class. A parent ⁠product⁠ class defines shared properties like ⁠name⁠, ⁠price⁠, and ⁠stock⁠, while child classes like ⁠PerishableProduct⁠ (with an ⁠expiration_date⁠ property) or ⁠WeightedProduct⁠ (sold per kilo) inherit these baseline properties and add their own specific fields. This eliminates redundant variable definitions across similar entities and keeps the inventory structure neat and scalable.
  
    class PerishableProduct(Product):
        def __init__(self, name: str, price: float, stock: int, expiration_date: str):
            super().__init__(name, price, stock)
            self.expiration_date = expiration_date

### 4. Polymorphism
 Polymorphism lets you use the same method name or interface to work with different types of objects, so each object can run its own unique code for that action⁠. While a standard item computes total cost simply as ⁠price * quantity⁠, a ⁠PerishableProduct⁠ can override ⁠calculate_total()⁠ to apply a clearance discount if the item is near expiration. This improves design by allowing the main sales module to process diverse items in a single list using a uniform method call, avoiding bloated ⁠if-else⁠ branching logic.   
    
    class PerishableProduct(Product):
        def calculate_total(self, quantity: int) -> float:
            discounted_price = self.price * 0.80
            return discounted_price * quantity

### REFLECTION:
Encapsulation is the most important pillar in improving the sari-sari store inventory system. In procedural programming, global or unmanaged variables result in errors such as negative stock counts or unauthorized price changes. Encapsulation will enforce strict validation and protect sensitive financial records from being accidentally corrupted by packaging the inventory data with specific access methods. Securing the integrity of data at the object level, so daily store transactions are accurate and reliable.




