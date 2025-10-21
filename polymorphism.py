class Vehicle:
    def __init__(self,wheels):
        self.wheels=wheels

    def sound(self):
        print("I am a vehicle")

class Bus(Vehicle):
    def sound(self):
        print("I am a bus")

class A:

    def add(self,a,b,c=0,d=0):
        return a + b + c + d
    
a = Bus(8)
a.sound()

b=A()
print(b.add(2,3,4,5))

