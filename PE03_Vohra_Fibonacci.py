#This program prints the Fibonacci series up to n numbers

def fibo(n):  #define a function to print Fibonacci series up to n numbers
    a = 0   #initialize the first number
    b = 1   #initialize the second number

    for i in range(n):  #loop through the range of n
        print(a, end="   ")    #print the current number in the series
        a, b = b, a + b     #update the values of a and b to the next two numbers in the series

n = int(input("How many Fibonacci numbers do you want? "))

fibo(n) #call the function to print Fibonacci series up to n numbers