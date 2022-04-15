from person import Person
from datetime import datetime,timedelta

class Customer (Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
    def checkout(self, data,book):
        condition=0
        for i in data[book]["estado"]:
            if i=="disponible":
                p=data[book]["estado"].index(i)
                data[book]["estado"][p]="arrendado"
                condition=1
                break
        if condition==1:
            return True
        else:
            return "ya se encuentran arrendados los ejemplares"
        
    def save_rental(self,condition,book):
        if condition==True:
            time1=int(input("cuantos dias va arrendar el libro: "))
            date1=input("fecha arriendo(año/mes/dia): ")
            date1=date1.split("/")
            date_rental=datetime(int(date1[0]),int(date1[1]),int(date1[2]))
            date_rental_out=date_rental + timedelta(time1)
            price=10*time1
            return[book,date_rental,date_rental_out,price]