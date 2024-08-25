"""
#
# Part: Python Class and Object
#
"""
# Build class
class MyClass:
    x = 5

# Call Class
object1 = MyClass()
print("Object1 =", object1.x)
object2 = MyClass()
print("Object2 =", object2.x)

class SpyXFamily:
    def __init__(self, name_f, age_f):
        self.name = name_f
        self.age = age_f

        def __str__(self):
           # return self.name + " - " + self.age
            return f"{self.name} - {self.age}"
        
    def sayHI(self, Last_name = "Tangyai"):
            print (f"Hey bruh what'sup {self.name} {Last_name}")
            
p1 = SpyXFamily("Akekarat", 20)
print(p1.name, p1.age)
print(p1)
p1.sayHI()


p2 = SpyXFamily("Ohm", 12)
print(p2.name, p2.age)
print(p2)
p2.sayHI("MOJOJO")

class Car:
     def __init__(self, body_color, engine_size):
          self.wheels = 4
          self.window = 4
          self.window_front = 1
          self.window_back = 1
          self.body_color = body_color
          self.engine_size = engine_size

     def push_window_button(self):
     # do someting
         pass
     
     def pop_window_butoon(self):
     # do someting
        pass

     def calspeed(self):
    # speed = self.engine_size * 1000
    # return speed
      return self.engine_size * 1000
     
     def turnOnFrontLight(self, status = "off"):
        if status == "on":
            # do someting
            pass
        else:
            # do someting
            pass
