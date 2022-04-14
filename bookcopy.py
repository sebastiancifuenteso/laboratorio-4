


class Book():
    def __init__(self,name,author,gender,serie):
        self.name=name
        self.author=author
        self.gender=gender
        self.serie=serie

    def save(self):
        return [self.name,self.author,self.gender,self.serie]


class Bookcopy():
    def __init__(self):
        self.data={}

    def facts(self,book):
        dicc={}
        data1=book.save()
        dicc["autor"]=data1[1]
        dicc["genero"]=data1[2]
        dicc["nombre"]=data1[0]
        dicc["estado"]="disponible"
        self.data[data1[3]]=dicc
        return self.data
    
    def delete_libro(self,book):
        data1=book.save()
        lista=[]
        for i in self.data:
            if data1[0]==self.data[i]["nombre"]:
                lista.append(i)
        for i in lista:
            self.data.pop(i)

    
    def delete_ejemplar(self,book):
        data1=book.save()
        self.data.pop(data1[3])



        

        


        

pp=Book(3,6,8,999)
k=Book(77,88,99,555)
hh=Book(77,0,0,0)
s=Bookcopy()

d=s.facts(pp)
f=s.facts(k)
e=s.facts(hh)
g=s.delete_libro(hh)
yy=s.delete_ejemplar(pp)
print(e)



