#Numeric Data Type
#int
x = 1

#float
y = 3.45
z = -7.9

#complex
z = 2 + 3j  # complex
print(z.real)  # Output: 2.0 (real part)
print(z.imag)  # Output: 3.0 (imaginary part)

#List Data type
lang = ["Python", "Java", "Kotlin"] # 3 string values
print(lang[2]) # Using index numbers to print out a specific language

#string
name = "Itumeleng"
print(name)

#Set Data Type
student_id = {111, 112, 113, 114, 115}

print(student_id)

print(type(student_id))

#Dictionary Data Type
student = {
    "id": 12345,   
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Physics", "Chemistry"]
}  #All these are {key:value}

#Dictionary values using key 
print(student["age"])

print(student["id"])
print()
#Type Conversion
#Implicit conversion
x = 10   # int
y = 3.5  # float

result = x + y  # Python automatically converts 'x' to float
print(result)
print(type(result))

#Explicit conversion
x = 10.7  # float

# Explicitly converting 'x' to an integer
x_int = int(x)  
print(x_int)
print(type(x_int))

print()

#Python operator

#Arithmetics operators-Define two numbers
a = 15
b = 4

# Addition
add = a + b
print(f"{a} + {b} = {add}")  

# Subtraction
subtract = a - b
print(f"{a} - {b} = {subtract}")

# Multiplication
multiply = a * b
print(f"{a} * {b} = {multiply}")

# Division
divide = a / b
print(f"{a} / {b} = {divide}")

# Floor Division
floor_divide = a // b
print(f"{a} // {b} = {floor_divide}")

# Modulo
mod = a % b
print(f"{a} % {b} = {mod}") 

# Exponentiation
exponent = a ** b
print(f"{a} ** {b} = {exponent}")

print()
#Assignemnt Operators
# Initial value
x = 10
print(f"Initial value of x: {x}")

# Simple assignment
x = 5
print(f"After x = 5: {x}")

# Add and assign
x += 3  # Equivalent to x = x + 3
print(f"After x += 3: {x}")

# Subtract and assign
x -= 2  # Equivalent to x = x - 2
print(f"After x -= 2: {x}")

# Multiply and assign
x *= 4  # Equivalent to x = x * 4
print(f"After x *= 4: {x}")

# Divide and assign (float result)
x /= 3  # Equivalent to x = x / 3
print(f"After x /= 3: {x}")

# Floor divide and assign (integer result)
x //= 2  # Equivalent to x = x // 2
print(f"After x //= 2: {x}")

# Modulo and assign
x %= 3  # Equivalent to x = x % 3
print(f"After x %= 3: {x}")

# Exponentiation and assign
x **= 2  # Equivalent to x = x ** 2
print(f"After x **= 2: {x}")

print()
#Comparison Operators
# Define two numbers
a = 10
b = 5

# Equal to
print(f"{a} == {b}: {a == b}")

# Not equal to
print(f"{a} != {b}: {a != b}")

# Greater than
print(f"{a} > {b}: {a > b}")

# Less than
print(f"{a} < {b}: {a < b}")

# Greater than or equal to
print(f"{a} >= {b}: {a >= b}")

# Less than or equal to
print(f"{a} <= {b}: {a <= b}")

print()
#Logical Operators
# Define two numbers
a = 5
b = 10
c = 15

# and operator: both conditions must be True
print(f"(a < b) and (b < c): {(a < b) and (b < c)}")  # True because 5 < 10 and 10 < 15

# or operator: at least one condition must be True
print(f"(a > b) or (b < c): {(a > b) or (b < c)}")    # True because b < c is True

# not operator: reverses the result of the condition
print(f"not(a > b): {not(a > b)}")                   # True because a > b is False, so not(False) is True

print()
#Printing Output and Collecting User Input in Python
print("Hello, world!")  #Basic Usage

name = "Alice" #F string
age = 25
print(f"Name: {name}, Age: {age}")

 # Collecting user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Printing output with formatted string
print(f"Hello, {name}! You are {age} years old.")



