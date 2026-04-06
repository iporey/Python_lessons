def Analyze_numbers():
    Numbers = []
    question = int(input("How many numbers do you like to use?: "))
    for i in range(question):
        num = int(input("Enter a number: "))
        Numbers.append(num)
    average = sum(Numbers) / len(Numbers)
    print(average)
    if not Numbers:
        print("No numbers entered.")
        return

    largest = Numbers[0]
    lowest = Numbers[0]
    for num in Numbers:
        if num > largest:
            largest = num
        if num < lowest:
            lowest = num
    print("Largest number: ", largest)
    print("Lowest numer is: ", lowest)


Analyze_numbers()
