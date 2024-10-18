# int ,float ,comlax
# str list tuple ("".'') [,,,''] (,,,'')
# dict {'':'','':'','':30}
# set {1,2,3}
# bool true or false

# Arithmetic Operators: +, -, *, /, %, ** (exponentiation), // (floor division).
# Comparison Operators: ==, !=, >, <, >=, <=.
# Logical Operators: and, or, not.
# Assignment Operators: =, +=, -=, *=, /=, etc.
# Bitwise Operators: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift).
# Membership Operators: in, not in (e.g., "a" in "apple").
# Identity Operators: is, is not (checks if two variables point to the same object).


# input
input("enter no : ")

print(".........................................................................................")
# assign variable
no=input("enter no :")
print(no)


print(".........................................................................................")
# print in betwwen statment
age=int(input("enter your age : "))
print("your age is ",age,"stay healty")



print(".........................................................................................")
# output
print("hellow")
print("...................................................................")

# use f to print variable value
name="pruthvi"
print(f"your name is \n:{name}")

rollno=73
print(f"roll no : {rollno}", sep="\n")

# blocks conditional,fuction,loop,exception handling block



# 1 conditional
age=int(input("enter age :"))
if(age==23):
    print("adult")
elif(age<=18):
    print("child")
else:
    print("old")    


#2loop
for i in range(5):
    print(i ,sep="\n")
print("...................................................")

# while loop

count = 0
while count<5 :
    print(count)
    count+=1

# 3funtion
def funct(name):
    print(f"your name is {name}")
funct("pruthvi")

# try block
try:
   x=10/0
except ZeroDivisionError:
    print("cannot divided by zero")
finally:
    print("exeption complete")

print ("........................................................")
try:
    # Trying to concatenate a string with an integer will cause a TypeError
    result = "The number is: " + 42
except TypeError:
    print("Type Error: You cannot add a string and an integer directly!")
finally:
    print("Execution complete.")




# 2.............................................................................................................


for i in range(10):
    if i==7:
        break
    print(i)

print("...................................................................................")
for i in range(10):
    if i==7:
        continue
    print(i)

print("...................................................................................")
for i in range(10):
    if i==7:
        pass
    print(i)


