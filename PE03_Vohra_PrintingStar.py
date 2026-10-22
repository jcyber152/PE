#This program will print Patterns with "*"

for i in range(5): #Repeat the loop 5 times to create 5 rows.
    print(" " * (4 - i) + "⭐ " * (i + 1)) #Prints spaces before the "⭐" to center the Triangle then prints more "⭐" as the row increases.