#1. Age Group Categorization

#Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+)
while True:
    age_group = int(input("Enter you age : "))
    if(age_group > 105 or age_group < 5 or age_group<1):
        print("invalid input enter correct age")
    else:
        if(age_group < 13):
            print("you are a child fuck off")
        elif(age_group >= 13 and age_group <= 19):
            print("you are a teenager fuck off")
        elif(age_group >= 20 and age_group <= 59):
            print("you are an adult go to work berojgar")
        elif(age_group >= 60):
            print("you are a senior please rest because you cant fuck")

    play = input("repeat : y\nexit : any key\n")
    if(play == 'y'):
        print("  ")
    else:
        break

