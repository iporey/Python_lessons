FullName = input("Enter your full name: ")
gender = input("Select gender (male/female):")

if gender.lower().strip == "male":
    print(f"Good morning, Mr. {FullName}")

elif gender.lower().strip == "female":
    print(f"Good morning, Ms. {FullName}")

else:
    print("Invalid gender selection")
