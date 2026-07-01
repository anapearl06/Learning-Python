# Customer Profile Management

# Create a dictionary
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# Print the dictionary
print("Original Dictionary:", customer)

# Add email and phone
customer["email"] = "john@example.com"
customer["phone"] = "1234567890"

# Print the updated dictionary
print("After Adding Email and Phone:", customer)

# Print name and city
print("Name:", customer["name"])
print("City:", customer["city"])

# Check if email exists
print("Does email exist?", "email" in customer)

# Delete age
del customer["age"]

# Print the updated dictionary
print("After Deleting Age:", customer)

# Print keys, values, and items
print("Keys:", customer.keys())
print("Values:", customer.values())
print("Items:", customer.items())

# Remove and print the last inserted key-value pair
last_item = customer.popitem()
print("Removed Item:", last_item)

# Access a non-existing key using .get()
membership = customer.get("membership")
print("Membership:", membership)

# Update the dictionary
customer.update({"address": "221B Baker Street"})

# Print the final dictionary
print("Final Dictionary:", customer)