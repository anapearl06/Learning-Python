def multiplication_table(number):
    table = []

    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")

    return table

number = int(input("Enter a number: "))

result = multiplication_table(number)

for line in result:
    print(line)