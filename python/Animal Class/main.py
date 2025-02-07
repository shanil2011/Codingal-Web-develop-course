from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class snake(animal):
    def move(self):
        print("I can crawl")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
R = human()
R.move()
k = snake()
k.move()
R = dog()
R.move()
k = lion()
k.move()