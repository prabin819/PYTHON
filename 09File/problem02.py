import random

with open("Hi-score.txt","r") as f:
        prevScore = f.read()
        if(prevScore==""):
             prevScore=0
score=int(prevScore)

def play():
    rand = random.randrange(0,10)
    return rand


newScore = play()
print(f"Your score is: {newScore}")


if(newScore>score):
    with open("Hi-score.txt","w") as f:
        f.write(str(newScore))

