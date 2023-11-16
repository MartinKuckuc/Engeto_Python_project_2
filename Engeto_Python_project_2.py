"""
Engeto_Python_project_2
author = Martin Kucirek
email = martin.kucirek89@gmail.com
Discord = Martin K.#3205
"""


import random

def generate_random_number():
    """
    Generate a random 4-digit number with unique digits.
    Returns:
        str: A string containing a 4-digit number with unique digits.
    """
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    
    # Ensure that '0' is not in the first position
    while digits[0] == '0':
        random.shuffle(digits)

    return ''.join(digits[:4])


def compare_numbers(secret, guess):
    """
    Compare the guessed number with the secret number and count bulls and cows.
    Args:
        secret (str): The secret 4-digit number.
        guess (str): The guessed 4-digit number.
    Returns:
        tuple: A tuple containing the number of bulls and cows.
    """
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows

def pluralize(count, singular, plural):
    """
    Format a count with the correct form for singular and plural.
    Args:
        count (int): The count to be formatted.
        singular (str): The singular form of the noun.
        plural (str): The plural form of the noun.
    Returns:
        str: The formatted count and noun.
    """
    if count == 0:
        return f"{count} {plural}"
    elif count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural}"

def play_bulls_and_cows():
    """
    Main function of the Bulls and Cows game.
    Generates a secret number, allows the player to make guesses, and provides feedback.
    """
    secret_number = generate_random_number()
    attempts = 0

    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    while True:
        guess = input("Enter a 4-digit number: ")

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) < 4 or guess[0] == '0':
            print("Please enter a valid 4-digit number without duplicates, starting with a non-zero digit.")
            continue

        attempts += 1
        bulls, cows = compare_numbers(secret_number, guess)
        print(f"{pluralize(bulls, 'bull', 'bulls')}, {pluralize(cows, 'cow', 'cows')}")

        if bulls == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} {pluralize(attempts, 'attempt', 'attempts')}.")
            break

if __name__ == "__main__":
    play_bulls_and_cows()
    