# Loan Eligibility Checker

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))

if age >= 21:
    if income >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible: Income too low")
else:
    print("Not eligible: Age must be 21 or above")