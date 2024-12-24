import random
computer=random.choice([1,0,-1])
print("choose from snake , water , gun")
yourchoice=input("enter your choice:")
yourdict={"snake":1,"water":0,"gun":-1}
reversedict={1:"snake",0:"water",-1:"Gun"}
you=yourdict[yourchoice]
print(f"you chose {reversedict[you]}\n Computer chose {reversedict[computer]}")
if (computer==you):
    print("its a draw")
else:
    if(computer==1 and you==0):
        print("you lose!Computer won")
    elif(computer==1 and you==-1):
        print("you won!Computer lose!")
    elif(computer==0 and you==1):
        print("you won!Computer lose")
        
        
    elif(computer==0 and you==-1):
        print("you lose!Computer won!")
    elif(computer==-1 and you==1):
        print("Computer won!You lose!")
    elif(computer==-1 and you==0):
        print("Computer lose!You won!")
    else:
        print("something went wrong")