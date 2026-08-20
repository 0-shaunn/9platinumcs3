# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation assorts product properties such as `name`, `price`, and `stock` into a single `Product` class while restricting direct access to these attributes. By making these variables private and exposing controlled public methods like `update_stock()` or `get_price()`, the system ensures that values cannot be set to invalid states, such as negative stock counts. This improves code organization by centralizing data validation within the class itself rather than scattering procedural checks throughout the codebase.

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
class PerishableProduct(Product):
    def __init__(self, name: str, price: float, stock: int, expiration_date: str):
        super().__init__(name, price, stock)
        self.expiration_date = expiration_date

### 4. Polymorphism
class PerishableProduct(Product):
    def calculate_total(self, quantity: int) -> float:
        discounted_price = self.price * 0.80
        return discounted_price * quantity

### REFLECTION:
Encapsulation is the most important pillar in improving the sari-sari store inventory system. In procedural programming, global or unmanaged variables result in errors such as negative stock counts or unauthorized price changes. Encapsulation will enforce strict validation and protect sensitive financial records from being accidentally corrupted by packaging the inventory data with specific access methods. Securing the integrity of data at the object level, so daily store transactions are accurate and reliable.




