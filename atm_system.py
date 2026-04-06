""" "
Simulation of the basic operation of an Automated Teller Machine(ATM)
"""

balance = 0
Correct_PIN = 2020
attempt = 3
print("\n=======WELCOM TO THE ATM BANK=========")
while True:
    PIN = int(input("ENTER YOUR PIN: "))
    if PIN == Correct_PIN:
        while True:
            print("\nWelcome to the menu")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit Menu")

            choice = input("Enter your menu choice: ")

            if choice == "1":
                print(f"current balance is: {balance}")

            elif choice == "2":
                deposit_money = float(input("Enter deposit amount: "))
                if deposit_money <= 0:
                    print("invalid amount")
                else:
                    balance += deposit_money
                    print(f"You have successfully deposited {deposit_money}")
                    print(f"Current balance is {balance} ")

            elif choice == "3":
                withdraw_money = float(input("Enter withdrawal amount: "))
                if withdraw_money <= 0:
                    print("Invalid amount entered!")
                elif withdraw_money > balance:
                    print("Insufficient funds")
                else:
                    balance -= withdraw_money
                    print(f"You have successfully withdrawn {withdraw_money}")
                    print(f"Current balance is {balance} ")

            elif choice == "4":
                print("Goodbye!!!")
                print("Thank you, have a nice day!")
                break

            else:
                print("Invalid choice!")
        break

    else:
        if attempt == 1:
            print("Incorrect Pin, ")
            print("You have exceeded your attempts, contact costumer care.")
            break
        else:
            attempt -= 1
            print(f"{attempt} attempt left")
