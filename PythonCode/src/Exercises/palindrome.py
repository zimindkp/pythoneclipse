# K Parekh Feb 2021
# Check if a string or number is a palindrome

#function to check if number is prime    
def isPalindrome(n): 
    # Reverse the string 
    # We create a slice of the string that starts at the end and moves backwards
    # ::-1 means start at end of string, and end at position 0 (the start), move with step -1 (1 step backwards)
    litmus = n[::-1]
    
    # Here is an example slice that starts from position 0 and goes till character 4
    litmus2 = n[:4]
    
    print(litmus, "is the reversed string")
    print(litmus2, "is another string")
    if (litmus == n):
        return True
    else:
        return False
    
# Driver Program
# Enter number here 
tester = input("Enter a string\n")
#Run the command


if (isPalindrome(tester)):
    print (tester, "is a Palindrome")
else: 
    print (tester, "is NOT a Palindrome")
    