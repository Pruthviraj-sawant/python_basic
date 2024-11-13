# # if-else
# a=input("enter no 1:")
# b=input("enter no 2:")
# c=input("enter no 3:")

# if(a>b and a>c):
#         print("A is greater")
# elif(b>a and b>c):
#         print("b is greater")     
# else:
#         print("c is greater")          

# #boolean
# p=(input("enter p : "))
# s=(input("enter s : "))
# if(p=="pruthvi"):
#     print("true")
# elif(s=="sawant"):
#     print("true")
# else:
#     print("false")    

    #write a program that reads a value of n and check the number is 0 or non zero value
    #write a program that read the number that no check is positive or negative
    #to check inter charachter is voewl or consoent
     #no even or odd
    #leap year or no
#smallest no amoung three
#evaluate student performance as 80 70 60 


    #1
# n=int(input("enter a no : "))
# print("you enter :",n)
# if(n==0):
#     print("the no is zero")

# else:  
#     print("not a zero")

    #2
# m=int(input("enter a no : "))
# print("your no :",m)
# if(m<0):
#     print("the no is negative")
# else:
#     print("the no is positive ")    
#3
# p=input("enter charachters :")
# print("your charachter : ",p)
# if(p=='a' or p=='e'  or p=='i' or p=='o' or p=='u' ):
#     print("the character is vowel ")
# else:
#     print("character is not vowel")

#4
# s=int(input("enter a no : "))
# print("your no : ",s)
# if(s%2 == 0):
#     print("the no is even.")
# else:
#    print("the no is odd")    

#5
# year=int(input("enter year"))
# print("year :",year)
# if(year%4==0 or year%100==0):
#     print("leap year")
# else:
#     print("not leap year")    

#6
# a=input("enter no 1:")
# b=input("enter no 2:")
# c=input("enter no 3:")

# if(a<b and a<c):
#         print("A is smaller :",a)
# elif(b<a and b<c):
#         print("b is smaller :",b)     
# else:
#         print("c is smaller :",c)       

#7
# c=input("enter name of stuednt :")
# d=float(input("enter percentage :"))
# print(c)
# print(d)
# if(d>95.00):
#      print("excellent")
# elif(d>80.00):
#      print("very very good")     
# elif(d>70.00):
#      print("very good")   
# elif(d>60.00):
#      print("good")   
# elif(d<60.00):
#      print("try again ")    
# else:
#      print("you loss sry!")        
       

     #   write a program to pritn natural no upto n in python
     # even non
     # odd non
     # sum of natural no
     # sum of odd and even 
     # natural no in reverse
     # fibonacci
     # fact
     # prime non
     # sum of digit
     # enter string is palindrom
     # multiply table
     # reverse given no
    


     #1

   
# n = int(input("Please Enter any Number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print("The factorial  is : ", end="")
# print(fact)

a={"fruite":"mange","flower":"rose"}
a[0]={"pry":"sry"}
print(a)


#python built in function
x = abs(-7.25)
print(x)

#all
mylist = []
x = all(mylist)
print(x)

#string methods
x="qillain"
p=x.capitalize()
r=x.casefold()	
s=x.center(5)	
t=x.count("pruthvi")	
u=x.encode()	
v=x.endswith("n")
print(x.lower())


print(p,r,s,t,u,v)
#list
listt=["orange","mango","banana"]
p=listt.append("sami")
print(p)
listt.reverse()
print(listt)
pruthvi=["pruthvi","sawant"]
x=pruthvi.copy()
print(x)
#######################################################################################################

#tuple
thistuple=(1,2,3,4,5,5,5,5,5,5,5,5,5)
x=thistuple.count(5)
print(x)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(thistuple)
print(len(thistuple))
thistuple = ("apple")
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
# Define a tuple
person = ("Alice", 30, "Engineer")

# Accessing elements of the tuple directly
name = person[0]
age = person[1]
profession = person[2]

# Displaying tuple information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Tuples are immutable, so to change a value, create a new tuple
new_profession = "Data Scientist"
person = (name, age, new_profession)

# Displaying updated tuple information
print("\nAfter updating profession:")
print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"Profession: {person[2]}")

# ###############################################################################################################################
# get_strings_methods()

# 1. capitalize
text = "hello EVERYONE"
print(text.capitalize())

# 2. case-fold
text1 = "heLLo"
text2 = "HELlo"
print(text1.casefold())
print(text2.casefold())

# 3. center
text3 = "DJ"
print(text3.center(26, "_"))

# 4. count
text4 = "abc_abc_abc_abc_abc"
print(text4.count("ab"))

# 5. encode
text5 = "Elon Musk"
print(text5.encode(encoding="UTF-8", errors="strict"))

# 6. endswith
text6 = "Apple"
print(text6.endswith("e"))

# 7. expend-tads
text7 = "Hello \tEveryone \tI'm DJ."
print(text7.expandtabs(20))

# 8. find
text8 = "My name is DJ."
print(text8.find("DJ"))

# 9. format
text9 = "{0}, My mane is {1}"
print(text9.format("Hello everyone!", "DJ"))

# 10. format_map
age: dict = \
    {"x": 45,
     "y": 10}
text10 = "Joel is {x} and Elie is {y}"
print(text10.format_map(age))

# 11. index
text11 = "Hello"
index_num = text11.index("l")
print(index_num)

# 12. is_al_num
text12 = "10"
text13 = "Dj-03"
print(text12.isalnum())
print(text13.isalnum())

# 13. is_alpha
text14 = "Hello"
text15 = "10"
print(text14.isalpha())
print(text15.isalpha())

# 14. is_a_scii
text14 = "Hello"
text16 = "HeLLė"
print(text14.isascii())
print(text16.isascii())

# 15. is_decimal
text17 = "123"
print(text17.isdecimal())

# 16. is_digit
text18 = "765"
text19 = "123"
print(text18.isdigit())
print(text19.isdigit())

# 17. is_numeric
text17 = "875"
text18 = "123"
text20 = "879"
print(text17.isdigit())
print(text18.isdigit())
print(text20.isnumeric())

# 18. is_identifier
text21 = "textSample"
print(text21.isidentifier())

# 19. is_lower
text22 = "abc"
print(text22.islower())

# 20. is_printable
text23 = "text"
print(text23.isprintable())

# 21. is_space
text24 = "    "
print(text24.isspace())

# 22. is_title
text25 = "The Text"
print(text25.istitle())

# 23. is_upper
text26 = "THE"
print(text26.isupper())

# 24. join
x = ["A", "B", "C"]
print("_".join(x))

# 25. l_just
text27 = "A"
print(text27.ljust(99, "_"))

# 26. lower
text28 = "FUN"
print(text28.lower())

# 27. l strip
text29 = "Some text."
print(text29.lstrip('Some'))

# 28. & 29. make_trans & translate
dic = {"I": "nh"}
text30 = "Hello, I Dj."
table = text30.maketrans(dic)

print(table)
print(text30.translate(table))

# 30. partition
text31 = "a+b= c^2"
print(text31.partition("="))

# 31. remove_prefix
text32 = "Endanger"
print(text32.removeprefix("En"))

# 32. remove_suffix
text33 = "Happiness"
print(text33.removesuffix("ness"))

# 33. replace
text34 = "Remember to comment & comment!"
print(text34.replace("comment", "subscribe", 1))

# 34. r_find
text35 = "An apple a day keeps a doctor away!"
print(text35.rfind("a"))

# 35. r_index
text35 = "An apple a day keeps a doctor away!"
print(text35.rindex("a"))

# 36. r_just
text36 = "A"
print(text36.ljust(99, "_"))

# 37.
text37 = "a+b = c^2 = z^2"
print(text37.rpartition("="))

# 38. & 39.
text38 = "Hello everyone good morning."
print(text38.rsplit(sep=" "))
print(text38.split(maxsplit=2))

# 40.
text39 = "I'm Dj Dj."
print(text39.rstrip("Dj"))

# 41.
text40 = "Remember to comment\n or else...\n"
print(text40.splitlines(keepends=True))
print(text40.splitlines())

# 42.
text41 = "Hello"
print(text41.startswith("H"))
print(text41.startswith("h"))

# 43.
text42 = "Hello everyone good morning"
print(text42.strip("Hello"))

# 44.
text43 = "Hello everyone good morning"
print(text43.swapcase())

#frozenset
fruits = frozenset(["apple", "banana", "orange"])

print("orange" in fruits)  

print(len(fruits)) 
more_fruits = frozenset(["grape", "kiwi"])
combined_fruits = fruits.union(more_fruits)
print(combined_fruits)  
common_fruits = fruits.intersection(more_fruits)
print(common_fruits)  
diff_fruits = fruits.difference(more_fruits)
print(diff_fruits)  
print(fruits.issubset(combined_fruits))  
print(combined_fruits.issuperset(fruits)) 
print(fruits.isdisjoint(more_fruits))  

sym_diff_fruits = fruits.symmetric_difference(more_fruits)
print(sym_diff_fruits) 
for fruit in fruits:
    print(fruit)

print(str(fruits))  # Output: frozenset({'banana', 'orange', 'apple'})​
print(hash(fruits))


#################################################################################################################################

# Define a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}

# Accessing and displaying dictionary information
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Profession: {person['profession']}")

# Updating a value in the dictionary
person['profession'] = "Data Scientist"

# Displaying updated dictionary information
print("\nAfter updating profession:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Profession: {person['profession']}")

arr = [1, 2, 3, 4, 5]

# Slicing
print(arr[1:4])  # Output: [2, 3, 4]
