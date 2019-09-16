#!/home/winher/ENV36/bin/python
#

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("Guess: "))
    if number > answer:
        print("Too big!")
    elif number < answer:
        print("Too small")
    else:
        print("It's Right")
        break
print("You guess count is %d ! " % counter)
