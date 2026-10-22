#This program calculates the price of a movie ticket based on the age of the customer
age = int (input("Enter your age: ")) #take input from the user for their age

while True:
    if age<3:
        print("Your ticket is free!") #if the age is less than 3, the ticket is free
        break
    elif age<=12:                     #if the age is less than 12, the ticket is $10
        print("Pay $10")
        break
    else:                             #if the age is greater than 12, the ticket is $15
        print("Pay $15")
        break