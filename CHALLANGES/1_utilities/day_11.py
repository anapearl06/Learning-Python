"""
=========================================
Day 11 : Friendship & Love Calculator
=========================================

A fun calculator that estimates friendship
or love compatibility based on two names.

⚠️ Just for entertainment!

Concepts Covered:
✔ Functions
✔ Sets
✔ Loops
✔ Conditional Statements
✔ String Methods
"""


# Step 1 : Calculate Compatibility

def calculate_score(name1, name2):
    """Returns a compatibility score between 0 and 100."""

    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    score = 0

    # Shared letters
    shared_letters = set(name1) & set(name2)
    score += len(shared_letters) * 8

    # Shared vowels
    vowels = {"a", "e", "i", "o", "u"}
    score += len(shared_letters & vowels) * 10

    # Matching characters at the same position
    for first, second in zip(name1, name2):
        if first == second:
            score += 7

    return min(score, 100)


# Step 2 : Display Result

def show_result(score):

    print("\n" + "=" * 50)
    print("❤️ COMPATIBILITY REPORT ❤️".center(50))
    print("=" * 50)

    print(f"\n💕 Compatibility Score : {score}%\n")

    if score >= 90:
        print("💍 Soulmates Alert!")
        print("✨ A perfect match. Chai ☕ & Samosa 🥟 vibes!")

    elif score >= 75:
        print("❤️ Amazing Chemistry!")
        print("🌸 You both make a wonderful pair.")

    elif score >= 60:
        print("😊 Great Friends!")
        print("🤝 Strong friendship with lots of fun.")

    elif score >= 40:
        print("😄 Good Connection!")
        print("🌟 Opposites sometimes attract.")

    elif score >= 20:
        print("🤔 Needs More Time!")
        print("🍕 Maybe start with coffee or pizza first.")

    else:
        print("😂 Very Different!")
        print("🎭 But who knows? Miracles happen!")

    print("\n" + "=" * 50)


# Step 3 : Main Program

print("=" * 50)
print("❤️ FRIENDSHIP & LOVE CALCULATOR ❤️".center(50))
print("=" * 50)

first_name = input("Enter First Name : ").strip()
second_name = input("Enter Second Name: ").strip()

compatibility_score = calculate_score(first_name, second_name)

show_result(compatibility_score)