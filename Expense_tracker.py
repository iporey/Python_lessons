expenses = {}  # {category : [amounts]}
categories = set()

print("======Expense Tracker======")

while True:
    print("\n1. Add Expense")
    print("2. View Summury")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        category = input("Enter category (Food, transport, ect): ")
        if category not in categories:
            categories.add(category)
            expenses[category] = []

        amount = float(input("Enter amount: "))
        expenses[category].append(amount)

        print("expense added")

    elif choice == "2":
        total = 0
        highest = ("", 0)  # (category, amount)

        print("\n-----Summury-----")
        for category, amount in expenses.items():
            category_total = sum(amount)
            total += category_total

            print(f"{category} : {category_total:.2f}")
            if category_total > highest[1]:
                highest = (category, category_total)
        print(f"\nTotal spending: {total:.2f}")
        print(f"Highest category: {highest[0]} ({highest[1]:.2f})")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
