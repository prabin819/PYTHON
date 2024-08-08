import random

a = random.randrange(1, 100)
# print(type(a))

userGuess = int(input("Guess a number between 1 and 100"))
noOfGuesses = 1

while(a!=userGuess):
    if(userGuess>a):
        print("Go lower")
    elif(userGuess<a):
        print("Go higher")
    
    userGuess = int(input("Guess a number"))
    noOfGuesses+=1

print(f"Congrats, your guess is correct. The number is {a} and it took you {noOfGuesses} guesses")