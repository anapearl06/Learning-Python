"""
=========================================
Day 4 : Minutes Alive Calculator
=========================================

Calculate approximately how long a person has
been alive based on their age in years.

Concepts Covered:
✔ Functions
✔ Loops
✔ Exception Handling
✔ Mathematical Calculations
✔ Number Formatting
"""


# Step 1 : Helper Function

def calculate_age(age_in_years):
    """Returns the approximate days, hours, and minutes lived."""

    DAYS_PER_YEAR = 365.25
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60

    total_days = age_in_years * DAYS_PER_YEAR
    total_hours = total_days * HOURS_PER_DAY
    total_minutes = total_hours * MINUTES_PER_HOUR

    return (
        round(total_days),
        round(total_hours),
        round(total_minutes)
    )


# Step 2 : Main Program


while True:

    try:
        age = float(input("Enter your age (in years): "))

        # Prevent negative age values.
        if age < 0:
            print("❌ Age cannot be negative.\n")
            continue

        days, hours, minutes = calculate_age(age)

       
        # Step 3 : Display Results

        print("\n" + "=" * 45)
        print("MINUTES ALIVE REPORT")
        print("=" * 45)

        print(f"📅 Days Lived     : {days:,}")
        print(f"⏰ Hours Lived    : {hours:,}")
        print(f"⏱️ Minutes Lived : {minutes:,}")

        print("=" * 45)

        
        # Step 4 : Ask to Continue

        choice = input("\nWould you like to calculate again? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThank you for using Minutes Alive Calculator! 👋")
            break

    except ValueError:
        print("❌ Please enter a valid numeric age.\n")