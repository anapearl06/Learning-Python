"""
=============================================
Day 2 : Stylish Bio Generator
=============================================

Generate a modern Instagram/Twitter bio based on
user details and optionally save it as a text file.

Concepts Covered:
✔ User Input
✔ Functions
✔ Conditional Statements
✔ File Handling
✔ String Formatting
"""

import textwrap


# Step 1 : Collect User Details

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your one-line passion: ").strip()
emoji = input("Enter your favorite emoji (optional): ").strip()
website = input("Enter your website/handle (optional): ").strip()

# Provide default values if optional fields are left empty.
emoji = emoji if emoji else "✨"
website = website if website else "No handle provided"


# Step 2 : Choose Bio Layout

print("\nChoose a Bio Style:")
print("1. Simple")
print("2. Vertical Flair")
print("3. Emoji Sandwich")

style = input("Enter your choice (1/2/3): ").strip()


# Step 3 : Generate Bio

def generate_bio(style):
    """Returns a formatted bio based on the selected style."""

    if style == "1":
        return f"""
{emoji} {name} | {profession}
💡 {passion}
🔗 {website}
"""

    elif style == "2":
        return f"""
{emoji} {name}
🔥 {profession}
💭 {passion}
🔗 {website}
"""

    elif style == "3":
        return f"""
{emoji * 3}
{name} • {profession}
{passion}
{website}
{emoji * 3}
"""

    else:
        return "Invalid style selected."

bio = textwrap.dedent(generate_bio(style)).strip()


# Step 4 : Display Bio

print("\n" + "=" * 45)
print("YOUR STYLISH BIO")
print("=" * 45)
print(bio)
print("=" * 45)


# Step 5 : Save Bio (Optional)

save = input("\nDo you want to save this bio? (y/n): ").strip().lower()

if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(bio)

    print(f"\nBio saved successfully as '{filename}'")

else:
    print("\nBio was not saved.")