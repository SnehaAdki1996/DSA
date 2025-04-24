from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def welcome(self):
        print("Welcome to ABC world")

class Laptop(Computer):
    def process(self):
        print("Processing-----")


l1 = Laptop()

l1.process()
l1.welcome()