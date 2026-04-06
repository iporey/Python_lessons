countries = ["America", "Canada", "Australia", "China", "Chile"]
for c in countries:
    if c.startswith("C"):
        countries.remove(c)
print(countries)
