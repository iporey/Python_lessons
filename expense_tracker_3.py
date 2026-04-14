""" "AN EXPENSE TRACKER"""

from typing import List

expenses: List = []
category_total: dict[str, float] = {}

print("=======Expense Tracker=========")
while True:
    print("\n1. Add expense")
    print("2. View expense")
    print("3. Total spending")
    print("4. Spending by category")
    print("5. Exit")

    choice: str = input("Choose Option: ")
    match choice:
        case "1":
            name: str = input("Enter expense name: ")
            amount: float = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Invalid amount entered")
            else:
                category = input("Enter expense category: ")

                expense_record: dict[str, str | float] = {
                    "name": name,
                    "amount": amount,
                    "category": category,
                }

                expenses.append(expense_record)
                try:
                    category_total[category] += amount
                except:
                    category_total[category] = amount
                print("Expense Added Successfuly.")

        case "2":
            if not expenses:
                print("No expenses yet")
            else:
                for expense in expenses:
                    print(expense["name"], expense["amount"], expense["category"])

        case "3":
            if not expenses:
                print("No expenses yet")
            else:
                total: float = 0
                for expense in expenses:
                    total += expense["amount"]
                print(total)

        case "4":
            for category in category_total:
                print(category, category_total[category])

        case "5":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")
            continue
