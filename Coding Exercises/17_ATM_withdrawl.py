# ATM Withdrawal Simulator

def atm_withdrawal_simulator(balance, withdrawals):
    messages = []
    i = 0

    while i < len(withdrawals):
        amount = withdrawals[i]

        if balance >= amount:
            balance -= amount
            messages.append(f"Withdrawn: {amount}")
        else:
            messages.append(f"Insufficient funds for requested amount: {amount}")

        i += 1

    messages.append(f"Remaining Balance: {balance}")

    return messages

# Example
balance = 1000
withdrawals = [200, 500, 400]

result = atm_withdrawal_simulator(balance, withdrawals)

for message in result:
    print(message)