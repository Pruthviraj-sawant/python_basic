#Positional Arguments
def funex(name, message):
    print(f"{name}! {message}")
funex("prurhvi","Welcome to the Python Practical!\n")



#Keyword Arguments
def introduce(name, age, city):
    print(f"My name is {name}. I am {age} years old and I live in {city}.\n")

introduce(name="pruthvi",age=19,city="haryana")




#Default Parameter
def funex1(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

funex1("pruthviraj","Welcome")
print(funex1)




#Arbitrary Keyword Arguments
def funex2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
funex2(name="joe", age=20, city="mumbai")