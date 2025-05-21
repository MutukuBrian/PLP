#Positional Arguments:

def add(a, b):
    return a + b

print(add(3, 5))  # Output: 8


#Default Arguments:

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!


#Keyword Arguments:

def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))  # Output: My name is Bob, and I'm 25 years old.



#Recursive Functions
#A function can call itself, enabling recursive problem-solving.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120