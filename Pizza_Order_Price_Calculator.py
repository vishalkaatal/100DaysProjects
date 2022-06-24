#Build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2

elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3

elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3

else:
    print("Pizza Size selection is incorrect, please enter S, M, L")

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
