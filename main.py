from abc import ABC , abstractmethod

class animal(ABC):
    def move(self):
        pass

class fish(animal):
    def move(self):
        print("fishes move by swimming!!!!")

class bird(animal):
    def move(self):
        print("birds fly")

#objects
f1 = fish()
f1.move()
