from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
    @abstractmethod
    def checkout(self,book):
        self.leased_books=[]
    
    def mostrar(self):
        return (self.leased_books)




