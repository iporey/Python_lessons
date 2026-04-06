# loop
# for
countries = ["Ghana", "Togo", "Benin", "Nigeria", "Kenya", "Egypt", "Canada"]
for country in countries:
    # print(country)
    pass

for x in range(10):
    # print(x)
    pass

for i in range(len(countries)):
    # print(countries[i])
    pass

total_savings = 0
for _ in range(5):
    amount = float(input("Enter your savings: "))
    total_savings += amount

print(f"Total savings is GHS{total_savings}")
