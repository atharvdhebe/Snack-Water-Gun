import random

computer = random.choice([-1,0,1])
user = input("Enter your choice (snack, water, gun): ").lower()
youDict ={"snack":1,"water":-1,"gun":0}
reverseDict = {1:"snack",-1:"water",0:"gun"}
you = youDict[user]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if you == computer:
    print("It's a tie")
else:
    if(computer == 1 and you == 0):
        print("You win")
    elif(computer == 1 and you == -1):
        print("Computer wins")  
    elif(computer == -1 and you == 1):
        print("You wins")   
    elif(computer == -1 and you == 0):
        print("Computer wins")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("Computer wins")  
    else:
        print("Invalid input")