def calculate_bill(Cups, Price_Per_Cup):
    return Cups * Price_Per_Cup


my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 5: ", calculate_bill(2, 20))

