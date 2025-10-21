from abc import ABC, abstractmethod

class first(ABC):
    @abstractmethod
    def sayHello(self):
        pass

    def sayNamaste(self):
        print("Namaste")

class second(first):
    def sayHello(self):
        print("hello")

a = second()
a.sayNamaste() 