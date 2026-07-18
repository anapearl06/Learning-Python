"""
=========================================
Day 10 : Caesar Cipher
=========================================

Encrypt and decrypt secret messages using
the Caesar Cipher encryption technique.

Concepts Covered:
✔ Functions
✔ Loops
✔ String Manipulation
✔ ASCII Values
✔ Modulo Arithmetic
✔ Conditional Statements
"""


# Step 1 : Encrypt Message

def encrypt_message(message, shift_key):
    """Encrypts a message using the Caesar Cipher."""

    encrypted_text = ""

    for character in message:

        if character.isalpha():

            base = ord("A") if character.isupper() else ord("a")

            shifted_character = (
                (ord(character) - base + shift_key) % 26
            ) + base

            encrypted_text += chr(shifted_character)

        else:
            encrypted_text += character

    return encrypted_text


# Step 2 : Decrypt Message

def decrypt_message(message, shift_key):
    """Decrypts a Caesar Cipher message."""

    return encrypt_message(message, -shift_key)


# Step 3 : User Interface

print("=" * 45)
print("🔐 SECRET MESSAGE ENCRYPTOR")
print("=" * 45)

choice = input("Choose an option - Encrypt (E) or Decrypt (D): ").strip().lower()


# Step 4 : Perform Operation

if choice == "e":

    original_message = input("\nEnter your message: ")

    try:
        shift_key = int(input("Enter the secret key (1-25): "))

        encrypted_message = encrypt_message(original_message, shift_key)

        print("\n" + "=" * 45)
        print("🔒 ENCRYPTED MESSAGE")
        print("=" * 45)
        print(encrypted_message)

    except ValueError:
        print("❌ Please enter a valid numeric key.")

elif choice == "d":

    encrypted_message = input("\nEnter the encrypted message: ")

    try:
        shift_key = int(input("Enter the secret key (1-25): "))

        decrypted_message = decrypt_message(encrypted_message, shift_key)

        print("\n" + "=" * 45)
        print("🔓 DECRYPTED MESSAGE")
        print("=" * 45)
        print(decrypted_message)

    except ValueError:
        print("❌ Please enter a valid numeric key.")

else:
    print("❌ Invalid option. Please choose E or D.")