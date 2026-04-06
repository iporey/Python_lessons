""" "AN EXPENSE TRACKER"""

expenses = []

print("=======Expense Tracker=========")
while True:
    print("\n1. Add expense")
    print("2. View expense")
    print("3. Total spending")
    print("4. Spending by category")
    print("5. Exit")

    choice = input("Choose Option: ")
    if choice == "1":
        name = input("Enter your expense: ")
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Invalid amount entered")

        else:
            category = input("Enter expense category")

            expense_record = {
                "name": name,
                "amount": amount,
                "category": category,
            }

            expenses.append(expense_record)
            print("Expense Added Successfuly.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet")
        else:
            for expense in expenses:
                print(expense["name"], expense["amount"], expense["category"])

    elif choice == "3":
        if not expenses:
            print("No expenses yet")
        else:
            total = 0
            for expense in expenses:
                total += expense["amount"]
            print(total)

    elif choice == "4":
        category_total = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount
        for category in category_total:
            print(category, category_total[category])
