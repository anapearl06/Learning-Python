class CoffeeOrder:

    def __init__(self, coffee_type, sweetness, size):
        self.coffee_type = coffee_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["coffee_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        coffee_type, sweetness, size = order_string.split("-")
        return cls(coffee_type, sweetness, size)


order1 = CoffeeOrder.from_dict(
    {
        "coffee_type": "Latte",
        "sweetness": "medium",
        "size": "large"
    }
)

order2 = CoffeeOrder.from_string("Cold-low-small")

print(order1.__dict__)
print(order2.__dict__)