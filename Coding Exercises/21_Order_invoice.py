# Order Invoice Generator

def generate_invoice(customer_name="Guest", *items, **charges):
    invoice = []
    invoice.append(f"Invoice for {customer_name}:")

    if items:
        invoice.append("Items:")
        for item in items:
            invoice.append(f"- {item}")

    if charges:
        invoice.append("Charges:")
        for charge, amount in charges.items():
            invoice.append(f"{charge.capitalize()}: {amount}")

    total = sum(charges.values())
    invoice.append(f"Total Amount Due: ₹{total}")

    return "\n".join(invoice)


# Example 1
print(generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0))

print()

# Example 2
print(generate_invoice("Riya", tax=30.0))

print()

# Example 3
print(generate_invoice())

print()

# Example 4
print(generate_invoice("John", "Pizza", "Coke"))