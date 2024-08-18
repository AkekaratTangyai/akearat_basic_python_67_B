"""
#
# Part: Python Comment
#
"""

# this is a commmet
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)
"""
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)
"""

print("Hello World!!!")

"""
#
# Part: Python Variables
#
"""
x = 5           # Integer
y = "Hey Bruh"  # String
print(x, y)

x = str(3)
Y = int(5)
z = float(3)
print(type(x), type(y), type(z))

"""
#
# Part: Python Variables Names
#
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
my_var2 = "John"
# 2my_var = "John"
# my-var = "John"
# my var = "John"

# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"
"""
#
# Part: Python String
#
"""
x = "Hey Bruh"
print(x)

y = """
1 Hey Bruh
2 Hey Bruh
3 Hey Bruh
"""
print(y)

x = "Hey Bruh"
print(x[2])
print(len(x))
print("Hey" in x)
print("What'sup" not in x)
print(x.upper())
print(x.lower())

print(x.replace("Bruh", "Sis"))
print(x.split(" "))

a = "Apple"
b = "Company"
print(a + " " + b)


price = 20
word = f"Price: {price:.2f}"
print(word)
