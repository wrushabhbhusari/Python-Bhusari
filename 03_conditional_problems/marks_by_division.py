# display the marks with division made by badal 
while True:
    name = input("Enter you name :")
    percentage = int(input("Enter your percentage :"))

    if(percentage >=70):
        print(name + ' you are in first division')

    elif(percentage >= 60):
         print(name + ' you are in second division')
    elif(percentage >=45):
        print(name + ' you are in third division')
    else:
        print(name + ' you are failed')

    repeat = input("check it again: ")
    if(repeat == 'y'):
        continue
    else:
        break
