from book import Book

class Rental():
    def __init__(self,data):
        self.data=data

    def save(self,data,name,rent,bookname):
        dicc={}
        f1=str(rent[1]).split(" ")
        f2=str(rent[2]).split(" ")
        p=rent[3]
        if name in data:
            data[name][bookname]={"fecha_arriendo":f1[0],"fecha_devolucion":f2[0], "precio":p}
        else:
            dicc[bookname]={"fecha_arriendo":f1[0],"fecha_devolucion":f2[0], "precio":p}
            data[name]=dicc
        return data
    def mostrar(self,info,name):
        print()
        print("==datos==")
        print(f"nombre:{name}")
        for i in info[name]:
            print()
            print(f"nombre libro: {i}")
            for j in info[name][i]:
                print(f"{j}:{info[name][i][j]}")
        return ""
    
    def return_book(self,name,book,info):
        info[name].pop(book)
        return info




        

        


    
