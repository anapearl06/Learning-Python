# Age Verification System

def verify_age(age_str):
    age = int(age_str)
    return "Access Granted" if age >= 18 else "Access Denied"

# Take input from the user
age_str = input("Enter your age: ")

# Print the result
print(verify_age(age_str))