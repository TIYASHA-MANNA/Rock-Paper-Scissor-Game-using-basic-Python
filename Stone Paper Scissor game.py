import random as r
i=1
while(i!=0):
    b=int(input("For how many rounds you want to play: "))
    c=0
    x=0
    for j in range(b):
        print('''
Enter 1 for Stone.
Enter 2 for Paper.
Enter 3 for Scissor.
''')
        A=int(input("Enter Your Choice: "))
        d=r.randint(1,4)
        print("Computer Choice: ",d)
        if((A==1 and d==3) or (A==2 and d==1) or (A==3 and d==2)):
            print("You Win: +1 point")
            c=c+1
        elif(A==d):
            print("Draw!!!")
        else:
            print("You Loose: +0 point")
            x=x+1
    if(c>x):
        print("Congrats You Won the Game!!!")
    elif(c==x):
        print("Match Draw !!!")
    else:
        print("Computer Wins the game")
    print('''
Do you want to play Again
IF Yes then ENTER 1
ELSE ENTER 0''')
    i=int(input("Enter your Choice: "))
