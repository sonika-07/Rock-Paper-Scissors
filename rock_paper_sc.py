import random
options=['Rock','Paper','Scissors']
my_score=0
comp_score=0
my_choice=True
while True:
    my_choice=input("enter your choice:").capitalize()
    computer = random.choice(options)
    print("computer choice:",computer)
    if my_choice==computer:
        print("Match Drawn")
    elif my_choice=='Rock':
        if computer=='Scissors':
            my_score=my_score+1
            print("YAY! You rock...")
        else:
            comp_score=comp_score+1
            print("OOPS! Computer covered you...")
    elif my_choice=='Paper':
        if computer=='Rock':
            my_score=my_score+1
            print("YAY! You covered computer...")
        else:
            comp_score=comp_score+1
            print("OOPS! computer cut you...")
    elif my_choice=='Scissors':
        if computer=='Rock':
            comp_score=comp_score+1
            print("OHH! Computer smashed you...")
        else:
            my_score=my_score+1
            print("YAY! you cut computer")
    elif my_choice=="End":
        print("Final Scores:")
        print("Your Score:",my_score)
        print("Computer Score:",comp_score)
        if my_score>comp_score:
            print("Hurray! You Win")
        elif comp_score>my_score:
            print("Wohoo! Computer Wins")
        else:
            print("Drawn")
        break


