import random
n=random.randint(1,100)
tentativi=0
win=False
while not win:
    guess=int(input("prova a indovinare:"))
    tentativi=tentativi+1
    if guess==n:
        win=True
        print("hai vinto con",tentativi,"tentativi!")
    elif guess < n:
        print("troppo piccolo!")
    else:
        print("troppo grande!")


    

