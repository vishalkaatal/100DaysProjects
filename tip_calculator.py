print("Welcome to the tip calculator!")
amount = float(input("What was the total bill? $"))
tip = int(input("How much tip percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
pay = round(((((amount*tip)/100) + amount)/people),2)
final = "{:.2f}".format(pay)
print(f"Each person should pay: ${final}")