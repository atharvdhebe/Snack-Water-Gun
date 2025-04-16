'''
1 for Snack
-1 for Water
0 for Gun
'''

import random

computer = random.choice([-1,0,1])
user = input("Enter Your Choice : ")
youDict = {"snack":1,"water":-1,"gun":0}
reverseDict = {1:"snack",-1:"water",0:"gun"}

you = youDict[user]

print(f"you Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")
if you == computer:
    print("It's a Tie")
else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("Computer win")
    elif(computer == 1 and you == -1):
        print("Computer win")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 0 and you == -1):
        print("you win")    
    elif(computer == 0 and you == 1):
        print("Computer win")   
    else:
        print("Invalid Input")