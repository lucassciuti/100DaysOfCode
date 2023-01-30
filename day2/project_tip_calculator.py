print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
n_people = int(input("How many people to split the bill?"))
tip_pct = int(input("What percentage tip would you like to give? 10, 12 or 15?")) / 100

each_bill = total_bill * (1 + tip_pct) / n_people

print("Each person should pay: $" + str(each_bill))
