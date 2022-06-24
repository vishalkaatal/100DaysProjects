#write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")
first_total = T+R+U+E

L = name1.lower().count("l") + name2.lower().count("l")
O = name1.lower().count("o") + name2.lower().count("o")
V = name1.lower().count("v") + name2.lower().count("v")
E = name1.lower().count("e") + name2.lower().count("e")
second_total = L+O+V+E

love_score = int(str(first_total) + str(second_total))

if (love_score < 10) or (love_score >90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


