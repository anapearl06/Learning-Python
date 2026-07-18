"""
=========================================
Day 1 : Self-Introduction Script Generator
=========================================

This program collects basic information from the user
and generates a professional self-introduction.

Concepts Covered:
✔ User Input
✔ Variables
✔ f-Strings
✔ Clean Code
✔ String Formatting
"""


# Step 1 : Collect User Details

# Ask the user for their personal information.
# The strip() method removes unwanted spaces from the beginning and end.

name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()
college = input("Enter your college name: ").strip()
course = input("Enter your course/branch: ").strip()
skills = input("Enter your skills (comma separated): ").strip()
career_goal = input("Enter your career goal: ").strip()


# Step 2 : Generate Introduction

# Using an f-string makes the introduction easy to read
# and simple to customize later.

introduction = f"""
Hello everyone!

My name is {name} and I am {age} years old.

I am currently pursuing {course} from {college}.

My current skill set includes {skills}.

My career goal is to become {career_goal}.

Thank you for taking the time to know me!
"""


# Step 3 : Display the Result

print("\n" + "=" * 50)
print("YOUR GENERATED SELF INTRODUCTION")
print("=" * 50)

print(introduction)

print("=" * 50)
print("Program Completed Successfully!")