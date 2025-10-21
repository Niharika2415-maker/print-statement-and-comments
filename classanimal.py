from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class dog(animal):
    def move(self):
        print("i can bark")
r= human()
r.move()
r= dog()
r.move()
