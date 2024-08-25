"""
#
# Part: Python Function
#
"""
def myFunction():
    i = 1
    while i <= 5:
        print("Hello World ", i)
        i+=1
myFunction()
myFunction()

# parameter
def myName(name):
    print("My Name is " + name)
myName("Akekarat")
myName("Tangyai")

def myFullName(first_name = "Unknow", last_name = "Tangyai"):
    print("My Name is " + first_name + " " + last_name)
myFullName("Akekarat")
myFullName("Akekarat", "Tangyai")
myFullName("M", "Tangyai")
myFullName(last_name = "Tangyai", first_name = "Ohm")

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["Apple", "Banana", "Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))
