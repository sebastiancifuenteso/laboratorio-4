from person import Person
from datetime import datetime,timedelta


d1=datetime(2020,1,1)
d2=d1+timedelta(15)
print(d2)

class Employee (Person):
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
    def habilitado(self,data,book):
        for i in data[book]["estado"]:
            if i =="arrendado":
                p=data[book]["estado"].index(i)
                data[book]["estado"][p]="disponible"


        
    def save_rental(self,condition,book):
        if condition==True:
            time1=int(input("cuantos dias va arrendar el libro: "))
            date1=input("fecha arriendo(año/mes/dia): ")
            date1=date1.split("/")
            date_rental=datetime(int(date1[0]),int(date1[1]),int(date1[2]))
            date_rental_out=date_rental + timedelta(time1)
            price=10*0.6*time1
            return[book,date_rental,date_rental_out,price]

    def show_inventory(self,data):
        print("===Inventario===")
        for i in data:
            for j,p in zip(data[i]["numero de serie"],data[i]["estado"]):
                print(f"nombre: {i}  numero de serie: {j}  estado: {p}")
        return ""

    def delete_book(self,data,name):
        data.pop(name)
        return data

    def delete_ejemplar(self,data,name,code):
        position=data[name]["numero de serie"].index(code)
        data[name]["numero de serie"].pop(position)
        data[name]["estado"].pop(position)
        return data
    
    def filter(self,data,dato):
        for i in data:
            if data[i]["autor"]==dato or data[i]["genero"]==dato:
                for j,p in zip(data[i]["numero de serie"],data[i]["estado"]):
                    print(f"nombre: {i}  numero de serie: {j}  estado: {p}")
        return ""








