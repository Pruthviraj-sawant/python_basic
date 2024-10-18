# file = open("geeks.txt", "r") 
# print (file.read())

# file = open("geeks.txt", "w") 
# print(file.write("pruthviraj sawant"))

# file = open("geeks.txt", "a")
# print(file.write("sawant")) 

# file = open("geeks.txt", "a")
# print(file.write("sawant sss")) 






# # Writing to a file
# with open('geeks.txt', 'w') as file:
#     file.write("Hello, this is a file handling example.\n")
#     file.write("Writing some data into the file.\n")

# print("Data written to file successfully.")

# # Reading from a file
# with open('geeks.txt', 'r') as file:
#     content = file.read()
#     print("Reading from file:")
#     print(content)





# f=open("pruthvi.txt","x")

# f=open("pruthvi.txt","w")
# f.write("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# f=open("pruthvi.txt","r")
# print(f.read())
# f=open("pruthvi.txt","a")
# f.write("pruthvi here................")


import re

# Search for a pattern in a string
result = re.search(r'\d+', 'The price is 100 dollars')
print(result.group())  # Output: "100"

result = re.findall(r'\b\w{3}\b', 'The cat ran and the dog barked')
print(result)  # Output: ['The', 'cat', 'ran', 'the', 'dog']


text = "My phone number is 123-456-7890."
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(new_text)  # Output: "My phone number is XXX-XXX-XXXX."
