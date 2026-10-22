#This program shows a person's stage of life based on their age

age=int(input("Enter Your Age:")) #take input from the user for their age

if age<2:       #check if the age is less than 2
    print("You are a Baby!")
elif age<4:     #check if the age is less than 4
    print("You are a Toddler!")
elif age<13:    #check if the age is less than 13
    print("You are a Kid!")
elif age<20:    #check if the age is less than 20
    print("You are a Teenager!")
elif age<65:    #check if the age is less than 65
    print("You are an Adult!")
else:           #if the age is 65 or older
    print("You are Older!")

print("Have a Nice Day 😊")