"""
Gambling game using while loops and the random module
"""

import random

attempts = 3
print("======Gambling Game=====")
while True:
    random_number = random.randint(1, 10)
    choice = int(input("Guess a number (1-10): "))
    if choice == random_number:
        print("You win")

    else:
        print("Sorry try again")

    if attempts == 1:
        print("Game over")
        print("Try anoter time")
        break

    else:
        attempts -= 1
        print(f"{attempts} attempts left")
