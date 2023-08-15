import random
def game():
    score=random.randint(1,100)
    print(f"the score is {score}")
    return score
score=game()
with open("file1.txt","r") as f:
    hiscore=int(f.read())
if hiscore<score:
    with open("file1.txt","w") as f:
        f.write(str(score))

    
    
    
    
