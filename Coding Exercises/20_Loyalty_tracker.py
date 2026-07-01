# Loyalty Points Tracker

# Global variable
loyalty_points = 0

def process_transactions(transactions):
    global loyalty_points

    total = sum(transactions)

    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50

    apply_bonus()

    loyalty_points += total // 100

    return total

# Example
transactions = [400, 700]

final_total = process_transactions(transactions)

print("Final Total:", final_total)
print("Total Loyalty Points:", loyalty_points)