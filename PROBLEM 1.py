import random
import string

def generate_password(length):
    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each required set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to randomize the order
    random.shuffle(password)

    return "".join(password)

# Get user input
while True:
    try:
        length = int(input("Enter the desired password length (min 8): "))
        if length < 8:
            print("Password length must be at least 8 characters. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
password = generate_password(length)
print("Generated Password:", password)
