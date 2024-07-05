import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """
    Generates a random password.

    Args:
    - length (int): Length of the password (default is 12)
    - use_digits (bool): Whether to include digits in the password (default is True)
    - use_special_chars (bool): Whether to include special characters in the password (default is True)

    Returns:
    - password (str): Generated random password
    """
    characters = string.ascii_letters  # lowercase + uppercase letters

    if use_digits:
        characters += string.digits  # add digits '0-9'
    if use_special_chars:
        characters += string.punctuation  # add special characters

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    print("----------------------------------------")

    length = int(input("Enter the length of the password: "))
    use_digits = input("Include digits (0-9)? (yes/no): ").lower() in ['yes', 'y']
    use_special_chars = input("Include special characters (!@#$%&*, etc.)? (yes/no): ").lower() in ['yes', 'y']

    password = generate_password(length, use_digits, use_special_chars)
    print("\nYour generated password is:", password)

if __name__ == "__main__":
    main()
