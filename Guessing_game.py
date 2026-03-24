import random

# Computer picks a number

secret_number = random.randint(1, 100)

guess = 0

attempts = 0

found = False  # boolean

print("Welcome to Ibrahim Porey's guessing game")
print("Pick number between 1 and 100")

while not found:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        found = True
        print(f"You guessed it in {attempts} attempts")
