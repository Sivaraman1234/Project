from random import randint
t=['stone','paper','scissor','finish']
computer=t[randint(0,2)]
player=False
player_point=0
computer_point=0
while player==False:
    player=input("stone,paper,scissor?")
    if player==computer:
        print("Tie")
    elif player=='stone':
        if computer == 'paper':
            print("you lose!",computer,"covers",player)
            computer_point+=1
        else:
            print("you win!",player,"covers",computer)
            player_point+=1
    elif player=='paper':
        if computer == 'scissor':
            print("you lose!",computer,"cuts",player)
            computer_point+=1
        else:
            print("you win!",player,"cuts",computer)
            player_point+=1
    elif player=='scissor':
        if computer == 'stone':
            print("you win!",player,"smashes",computer)
            player_point+=1
        else:
            print("you lose!",computer,"smashes",player)
            computer_point+=1
    elif player=='finish':
        print("your score is",player_point)
        print("computer score is",computer_point)
        break
    player=False
    computer=t[randint(0,2)]

    
