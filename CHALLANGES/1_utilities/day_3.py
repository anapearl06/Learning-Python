"""
=========================================
Day 3 : Simple Bill Splitter
=========================================

Split a restaurant bill evenly among friends
and optionally validate user input.

Concepts Covered:
✔ User Input
✔ Lists
✔ Loops
✔ Functions
✔ Exception Handling
✔ String Formatting
"""


# Step 1 : Helper Function

def get_float(prompt):
    """Keeps asking until the user enters a valid number."""

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


# Step 2 : Collect Group Details

num_people = int(input("Enter the number of people: "))

people = []

for i in range(num_people):
    person_name = input(f"Enter name of person #{i + 1}: ").strip()
    people.append(person_name)


# Step 3 : Calculate Bill Share

total_bill = get_float("Enter the total bill amount (₹): ")

share_per_person = round(total_bill / num_people, 2)


# Step 4 : Display Summary

print("\n" + "=" * 45)
print("BILL SUMMARY")
print("=" * 45)

print(f"👥 Total People : {num_people}")
print(f"💰 Total Bill   : ₹{total_bill:.2f}")
print(f"💸 Each Pays    : ₹{share_per_person:.2f}")

print("\nAmount to be Paid:")

for person in people:
    print(f"• {person:<15} ₹{share_per_person:.2f}")

print("=" * 45)
print("Thank you! Have a great meal 🍽️")