class Coffeeorder:
    
    def __init__(self, size, type):
        self.size = size
        self.type = type    

    def summary(self):
        return f"Your order is a {self.size} {self.type} coffee."
    
order = Chaiorder = Coffeeorder("large", "chai")
print(order.summary())  # Your order is a large chai coffee.

order_two = Coffeeorder("small", "espresso")    
print(order_two.summary())  # Your order is a small espresso coffee.

