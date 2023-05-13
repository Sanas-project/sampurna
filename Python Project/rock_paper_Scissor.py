import random as r

print("WELCOME!!")

print("Enter 1 for choosing Rock \n Enter 2 for choosing Paper \n Enter 3 for choosing Scissor \n")

while True:
    user_ch =int(input("Enter your choice"))
    if(user_ch==1):
        print("You have choose Rock!\n") #printing the user choice accordingly elif(user_ch==2):
        print("You have choose Paper!\n")
    else:
        print("You have choose Scissors!\n")
        print("Now it's turn for computer's Choice\n")
# initializing the value of cp_ch variable
    cp_ch =r.randint(1,3) #Using randint method of random module
    if(cp_ch==1):
        print("Computer's choice: Rock!\n") #printing the random computer's choice
    elif(cp_ch==2):
        print("Computer's choice :Paper!\n")
    else:
        print("Computer's choice: Scissors!\n")
#conditions to win
    print("Now it's Time to Play")

    if((user_ch==1 and cp_ch==2) or (user_ch==1 and cp_ch==3) or (user_ch==3 and cp_ch==2)):
        print("User Wins!!")
    elif((user_ch==2 and cp_ch==2) or (user_ch==2 and cp_ch==3)or (user_ch==3 and cp_ch==1)):
        print("Computer Wins!!")
    #checking for draw
    elif(user_ch==cp_ch):
        print("It's a tie!")
    print("Do you want to play again (Y/N)?")
    a = input()
    #if input is N then the condition will be true and loop continues
    if(a=='N'):
        break
    print("Thanks for Playing!")