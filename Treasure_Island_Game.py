print('''
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                              
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n' ).lower()

if crossroad == "left":
  #continue to the game
  lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if lake == "wait":
    #continue to the game
    colour = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if colour == "red":
      print("It's a room full of fire. Game Over.")
      print('''
                                                                   
                      88            ad88 88                        
                      ""   ,d      d8"   ""                        
                           88      88                              
,adPPYba, 8b,dPPYba,  88 MM88MMM MM88MMM 88 8b,dPPYba,  ,adPPYba,  
I8[    "" 88P'    "8a 88   88      88    88 88P'   "Y8 a8P_____88  
 `"Y8ba,  88       d8 88   88      88    88 88         8PP"""""""  
aa    ]8I 88b,   ,a8" 88   88,     88    88 88         "8b,   ,aa  
`"YbbdP"' 88`YbbdP"'  88   "Y888   88    88 88          `"Ybbd8"'  
          88                                                       
          88                                                       
      ''')
    elif colour == "yellow":
      print("You found the treasure! You Win!")
    elif colour == "blue":  
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
    
  else:
    print("You have attached by an angry trout. Game Over")
else:
  print("Fall into a hole. \nGame Over")
  print('''
                                         
88                      88             
88                      88             
88                      88             
88,dPPYba,   ,adPPYba,  88  ,adPPYba,  
88P'    "8a a8"     "8a 88 a8P_____88  
88       88 8b       d8 88 8PP"""""""  
88       88 "8a,   ,a8" 88 "8b,   ,aa  
88       88  `"YbbdP"'  88  `"Ybbd8"'  
  
  ''')

