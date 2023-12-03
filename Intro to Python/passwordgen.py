import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    password = ""
    criteria = False
    has_numbers = False
    has_specials = False

    while not criteria or len(password) < min_length:
        randomchar = random.choice(characters)
        if randomchar in digits:
            has_numbers = True
        if randomchar in specials:
            has_specials = True
        
        if numbers and special_characters:
            criteria = has_numbers and has_specials
        elif numbers:
            criteria = has_numbers
        elif special_characters:
            criteria = has_specials
        else:
            criteria = True
        password += randomchar
    return password

def get_yes_no(x):
    choice = input(x).lower()
    while choice not in ("yes","no"):
        print('Error: Input must be "Yes  or "No" only.')
        choice = input(x).lower()
    return choice

def main():
    print("Welcome to Password Generator!")
    length = int(input("Enter the minimum length for your password: "))
    include_numbers = get_yes_no("Include numbers in the password? (Yes/No): ")
    include_specials = get_yes_no("Include special characters in the password? (Yes/No): ")

    numbers = True if include_numbers == "yes" else False
    specials = True if include_specials == "yes" else False

    generated_password = generate_password(length, numbers, specials)
    print(f"Your generated password is: {generated_password}")


if __name__ == '__main__':
    main()