Citizenship_status = input("Enter your country's name: ")
age = int(input("Enter your age: "))

if Citizenship_status.upper().strip() == "GHANA" and age >= 18:
    print("You are eleigible to vote")

else:
    print("Come back when your age is  18 years or above")
