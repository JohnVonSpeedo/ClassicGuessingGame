import random

num = random.randint(1, 100)
guess = 0

while guess != num:
    guess = int(input("Try to guess the mystery number: "))
    if guess > num:
        print(f"The mystery number is lower than {guess}")
    elif guess < num:
        print(f"The mystery number is higher than {guess}")
    else:
        print(f"You have guessed the mystery number {num}")