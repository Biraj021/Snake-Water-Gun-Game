import random
computer=random.choice([1,0,-1])
youstr=input("Enter your choice:")
youdic={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdic[youstr]
print(f"you chose {reversedict[you]}\ncoumputer chose{reversedict[computer]}")
if(computer==you):
    print("It's draw")
else :
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==0 and you==1):
        print("You Lose!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")