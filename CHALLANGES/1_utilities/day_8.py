"""
=========================================
Day 8 : Password Strength Checker
=========================================

Check whether a password is strong based on
common security rules and suggest a stronger
password if needed.

Concepts Covered:
✔ Functions
✔ String Module
✔ Random Module
✔ getpass Module
✔ Conditional Statements
✔ Password Validation
"""

import random
import string
import getpass


# Step 1 : Check Password Strength

def check_password_strength(password):
    """Returns a list of missing password requirements."""

    issues = []

    if len(password) < 8:
        issues.append("Password must contain at least 8 characters.")

    if not any(character.isupper() for character in password):
        issues.append("Missing an uppercase letter (A-Z).")

    if not any(character.islower() for character in password):
        issues.append("Missing a lowercase letter (a-z).")

    if not any(character.isdigit() for character in password):
        issues.append("Missing a digit (0-9).")

    if not any(character in string.punctuation for character in password):
        issues.append("Missing a special character (!,@,#,$...).")

    return issues


# Step 2 : Generate Strong Password

def generate_strong_password(length=12):
    """Generates a random strong password."""

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return "".join(random.choice(characters) for _ in range(length))


# Step 3 : Get User Password

password = getpass.getpass("Enter your password: ")

issues = check_password_strength(password)


# Step 4 : Display Result

print("\n" + "=" * 45)
print("PASSWORD STRENGTH REPORT")
print("=" * 45)

if not issues:

    print("✅ Your password is strong.")
    print("🔒 You're good to go!")

else:

    print("❌ Your password is weak.")
    print("\nImprovements Needed:")

    for issue in issues:
        print(f"• {issue}")

    print("\n💡 Suggested Strong Password:")
    print(generate_strong_password())

print("=" * 45)