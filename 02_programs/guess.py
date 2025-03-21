import random

attempts = 0 

while True:

    while True:
        guessNum= int(input("Enter the guess num : "))

        randNum = random.randrange(1,10)

        if(guessNum < 1 or guessNum > 10):
            print("Enter values in the range!")
            break
        else:
            if(guessNum == randNum):
                print("You guessed it write !!!")
                print("your attempts are ", attempts)
                break
            elif(guessNum < randNum):
                print("Too low!!")
            elif(guessNum > randNum):
                print("Too High!!")

    play = input("play : y \n no play : any key")
    if(play == "y"):
        attempts= 0
    else:
        break
