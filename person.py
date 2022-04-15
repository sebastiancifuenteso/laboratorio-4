from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
    @abstractmethod
    def checkout(self,book):
        pass




