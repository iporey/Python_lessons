"""
Random students selection program using the random module and a while loop
"""

import random

student_names = [
    "Michael Mensah",
    "David Amoah",
    "James Mumuni",
    "Bright Afful",
    "Esther Ampomaa",
    "Janet Blankson",
    "Bright Agyeman",
]

print("Random Student Selection")

while True:
    random_number = random.randint(0, len(student_names) - 1)
    choice = input("Enter 'start' to run the program or 'q' to quit: ")
    if choice.lower == "start" or "s" in choice.lower():
        print(f"Selected student: {student_names[random_number].title()}")
        if len(student_names) == 0:
            student_names.pop(random_number)
    # break
    elif choice.lower() == "q":
        print("Program closed")
        break
    else:
        print("Enter a valid option")
