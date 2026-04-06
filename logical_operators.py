# Logical operators
# AND , OR , NOT
# AND- both conditions must be true
# OR- any of the conditions can be true
# OR- At least one condition can be true
# NOT- negates the condition EG If a value is false, NOT will make it true and vice versa

# Schorlaship

gender = input("Enter you gender(male/female): ")
age = int(input("Enter your age: "))

if gender.lower().strip() == "female":
    print("congratulations you have been awarded a schorlaship")

elif gender.lower().strip() == "male" and age >= 25:
    print("congratulations you have been awarded a schorlaship")

else:
    print("You do not qualify for a schorlaship")
