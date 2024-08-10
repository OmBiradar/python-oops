import csv

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    def calcualte_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price').strip()),
                quantity=int(item.get('quantity').strip()),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e.: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return False
        else:
            return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
