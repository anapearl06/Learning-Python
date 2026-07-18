"""
=========================================
Day 5 : Emoji Enhancer for Messages
=========================================

Enhance a user's message by automatically
adding emojis after specific keywords.

Concepts Covered:
✔ Dictionaries
✔ Loops
✔ String Methods
✔ Conditional Statements
✔ Text Processing
"""


# Step 1 : Emoji Dictionary

emoji_map = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
    "coffee": "☕",
    "python": "🐍",
    "travel": "✈️",
    "book": "📚",
    "sleep": "😴",
    "party": "🎉",
}


# Step 2 : Get User Message

message = input("Enter your message: ")


# Step 3 : Enhance the Message

enhanced_words = []

for word in message.split():

    # Remove punctuation for keyword matching
    cleaned_word = word.lower().strip(".,!?")

    emoji = emoji_map.get(cleaned_word)

    if emoji:
        enhanced_words.append(f"{word} {emoji}")
    else:
        enhanced_words.append(word)

enhanced_message = " ".join(enhanced_words)


# Step 4 : Display Result

print("\n" + "=" * 50)
print("ENHANCED MESSAGE")
print("=" * 50)
print(enhanced_message)
print("=" * 50)