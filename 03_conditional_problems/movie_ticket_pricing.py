#2. Movie Ticket Pricing
#Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
import datetime

date = datetime.datetime.now()
discount_day = date.strftime("%A")
age = int(input("Enter your age : "))

ticket_price_adult = 12
ticket_price_children = 8
discount = 2

if (age < 1 or age > 100):
    print("Enter the correct age")
else:
    if(age >= 18):
         if(discount_day == 'wednesday'):
             print("your ticket prize is ", ticket_price_adult - discount)\
             
             