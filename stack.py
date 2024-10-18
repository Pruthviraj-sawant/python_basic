stack = []
top = 0

def push(num):
    global top  
    stack.append(num)
    top += 1

def pop():
    global top  
    if top == 0:
        return -1
    else:
        top -= 1
        return stack.pop()

def size():
    return top

def empty():
    if top == 0:
        return 1
    else:
        return 0

def peek():
    if top == 0:
        return -1
    else:
        return stack[top - 1]

def display():
    for i in stack:
        print(i, end=',')
    print()  # To add a newline after the list

# Test the stack operations
push(2)
push(5)
push(7)
display()  
print("Top element:", peek()) 
print("Stack size:", size())
print("Is stack empty?", empty())
pop()
display()