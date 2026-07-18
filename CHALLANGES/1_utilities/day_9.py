"""
=========================================
Day 9 : Countdown Timer
=========================================

Set a countdown timer in seconds and watch
the remaining time update live in the terminal.

Concepts Covered:
✔ Loops
✔ Exception Handling
✔ Time Module
✔ Input Validation
✔ MM:SS Formatting
"""

import time


# Step 1 : Get Timer Duration

while True:

    try:
        total_seconds = int(input("⏰ Enter timer duration (in seconds): "))

        if total_seconds <= 0:
            print("❌ Please enter a number greater than 0.\n")
            continue

        break

    except ValueError:
        print("❌ Please enter a valid whole number.\n")


# Step 2 : Start Countdown

print("\n🚀 Countdown Started...\n")

for remaining_seconds in range(total_seconds, 0, -1):

    minutes, seconds = divmod(remaining_seconds, 60)

    formatted_time = f"{minutes:02}:{seconds:02}"

    print(f"⏳ Time Remaining: {formatted_time}", end="\r")

    time.sleep(1)


# Step 3 : Timer Finished

print("\n" + "=" * 45)
print("⏰ Time's Up!")
print("🎉 Great job! Take a short break or start your next task.")
print("=" * 45)

# Optional beep sound (works in some terminals)
print("\a")