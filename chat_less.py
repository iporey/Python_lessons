# Write a programm that ask the user for
# 1 Three numbers
# 2 store them in a list
# 3 print the largest number

Numbers = []
for i in range(3):
    num = int(input("Enter a number: "))
    Numbers.append(num)
Lowest = Numbers[0]
for num in Numbers:
    if num < Lowest:
        Lowest = num
print("Lowest number is", Lowest)
# largest = Numbers[0]
# for num in Numbers:
#   if num > largest:
#      largest = num
# print("Largest number is", largest)
# print(max(Numbers))
# print(min(Numbers))

# average = sum(Numbers) / len(Numbers)
# print(average)
