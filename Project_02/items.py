import csv

class Item:
    all = []
    discount_rate = 0.5
    def __init__(self,name: str,price: float,quantity: int=0):        
        self.name = name
        assert price >=0, f"Price: {price} should be greater than zero."
        self.price = price
        assert price >=0, f"Quantity: {quantity} should be greater than zero."
        self.quantity = quantity
        
        Item.all.append(self)
        
    def __str__(self):
        return f"Item name: {self.name},Item price: {self.price},Item quantity: {self.quantity}"
    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
    def calculate_price(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.discount_rate
        return self.price
    
    @classmethod
    def instantiate_csv(cls):
        with open("items.csv",'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            
        for item in items:
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity'))
            )
        
# item_1 = Item() # object with no instance attributes
Item.instantiate_csv()
print(Item.all)