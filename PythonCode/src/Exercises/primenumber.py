# K Parekh Feb 2021
# Check if a number is prime in Python
# Using recursion


#function to check if number is prime    
def isPrime(n, i): 
    # check if number is 2, 1 is NOT a prime number fyi
    if(i==1):
        #print ("is prime")
        return True 
    # if the number is divisible by half its value, then not prime
    elif (n % i == 0):
        return False
    #otherwise, recursively call the program, reducing value of the divisor
    else:
        i = i-1
        return isPrime(n, i)

# Driver Program
# Enter number here 
n = int(input("Enter a positive integer\n"))
#Run the command
div = int(n/2)

if (isPrime(n, div)): 
    print (n, "is a prime number")
else: 
    print (n, "is NOT prime number")
    