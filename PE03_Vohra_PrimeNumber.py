#This code show how to find prime numbers.
#This program asks the user for a number, then checks numbers starting from 2. 
# For each one, it uses the % sign to see if there's any remainder. 
# If the remainder is zero, that means the number isn't prime, and the program stops checking.
# If none of the numbers divide evenly, the loop finishes and the program reports the number is prime.

#Takes input from user to check whether it's prime number or not
num = int(input("Enter a number : "))

# Check possible divisible number of the current number.
for i in range(2, num):
    if num % i == 0:  # Check if the number divides evenly.
        
    # Display the number as a product of two divisible number.
        print(num, "is not a prime number")

        break  # Stop checking this number and move to the next one.

else:
        # This runs if the inner loop finds no divisible number.
         print(num, "is a prime number")