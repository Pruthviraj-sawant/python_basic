#print even no from the list




def arithmetic_operation(a, b, operator):
    if operator == '+':
        return  a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operator"

# Examples of usage:
p=int(input("NO 1 :"))
s=int (input("NO 2 :"))
r=input("operation : ")
all=arithmetic_operation(p,s,r)
print(all)

















###############################vowel

char=input("enter charachter to check vowel or not : ")
def vowel(char):
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowell="this is vowel"
        return vowell
    else:
        return "this is not vowel"
    
print(vowel(char))    










############evenodd

no = int(input("Enter a number: "))
def evenodd(no):
    if no % 2 == 0:
        return "even number"
    else:
        return "odd number"

print(evenodd(no))







    ############fact
n = int(input("Enter a number: "))

def fact(n):
    factt = 1
    for i in range(1, n + 1):
        factt *= i
    return factt

print("The factorial is: ", end="")
print(fact(n))


############################lambda funtioon

# Addition
add = lambda x, y: x + y
# Subtraction
subtract = lambda x, y: x - y
# Multiplication
multiply = lambda x, y: x * y
# Division
divide = lambda x, y: x / y
# Usage examples
print("lambada function")
print(add(10, 5))       
print(subtract(10, 5)) 
print(multiply(10, 5))  
print(divide(10, 5))    





#################################even odd
def find_even_odd(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    return even_numbers, odd_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = find_even_odd(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)

