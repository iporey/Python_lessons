# break , continue

fruits = ["Apple", "Banana", "Grapes", "Orange", "Watermelon"]

# continue
print("======Using countinue======")
for fruit in fruits:
    if fruit == "Grapes":
        continue
    print(fruit)

# break
print("=====using break=====")
for fruit in fruits:
    if fruit == "Orange":
        break
    print(fruit)
