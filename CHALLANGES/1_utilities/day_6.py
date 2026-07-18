"""
=========================================
Day 6 : Daily Learning Journal Logger
=========================================

Store your daily learning progress in a journal
with a timestamp and an optional productivity rating.

Concepts Covered:
✔ User Input
✔ File Handling
✔ Date & Time
✔ String Formatting
✔ Append Mode
"""

from datetime import datetime


# Step 1 : Collect Journal Entry

learning_entry = input("What did you learn today? ").strip()
productivity_rating = input("Rate your productivity (1-5, optional): ").strip()


# Step 2 : Generate Timestamp

current_time = datetime.now()
timestamp = current_time.strftime("%d %B %Y | %I:%M %p")


# Step 3 : Prepare Journal Entry

journal_entry = f"""
📅 {timestamp}

📝 Today's Learning:
{learning_entry}
"""

if productivity_rating:
    journal_entry += f"\n⭐ Productivity Rating: {productivity_rating}/5"

journal_entry += "\n" + "=" * 50 + "\n"


# Step 4 : Save to File

with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)


# Step 5 : Confirmation Message

print("\n" + "=" * 45)
print("✅ Journal Entry Saved Successfully!")
print("📄 File Name : learning_journal.txt")
print("=" * 45)