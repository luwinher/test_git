#!/home/winher/ENV36/bin/python
#

from random import randint

money = 1000
debt = 100
while money > 0:
    win = False
    randint1 = randint(1, 6) + randint(1, 6)
    debt = int(input("Please put up stakes: "))
    print("You random number is %d." % randint1)
    if randint1 == 7 or randint == 11:
        money += debt
        win = False
    elif randint1 == 2 or randint == 3 or randint == 12:
        money -= debt
    else:
        while True:
            randint2 = randint(1,6) + randint(1,6)
            print("You random again is %d." % randint2)
            if randint2 == 7:
                money -= debt
                break
            elif randint2 == randint1:
                money += debt
                win = True
                break
            else:
                pass
    if win == True:
        print("You win, your money is %d." % money)
    else:
        print("You fail, your money is %d." % money)
print("You're bankruptcy!")
