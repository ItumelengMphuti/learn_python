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