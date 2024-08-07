import random
computerChoice= random.choice([-1,0,1])
youDict={
    "r":-1,
    "p":0,
    "s":1
}
reverseDict={
    -1:"rock",
    0:"paper",
    1:"scissors"
}
youStr = input("Enter your choice: r,p or s: ")
l=["r","p","s"]
if(not(youStr in l)):
    print("please enter correct choice")
yourChoice = youDict[youStr]
print(f"You chose {reverseDict[yourChoice]} \n computer chose {reverseDict[computerChoice]}")

if(computerChoice==yourChoice):
    print("Its a draw")
else:
    if(computerChoice==-1 and yourChoice==0):
        print("You win")
    elif(computerChoice==-1 and yourChoice==1):
        print("You lose")
    elif(computerChoice==0 and yourChoice==-1):
        print("You lose")
    elif(computerChoice==0 and yourChoice==1):
        print("You win")
    elif(computerChoice==1 and yourChoice==-1):
        print("You win")
    elif(computerChoice==1 and yourChoice==0):
        print("You lose")
    else:
        print("Something went wrong")