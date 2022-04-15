from book import Book
from bookcopy import Bookcopy
from customer import Customer
from person import Person
from employee import Employee
from rental import Rental

save1={}
rent={}
copy=Bookcopy(save1)
re=Rental(rent)
name1=Employee("sebastian","cifuentes")



while 3<4:
    print("==Menu biblioteca==")
    print("1)Inventario")
    print("2)Agregar libro")
    print("3)Eliminar libro o ejemplar")
    print("4)Arrendar libro")
    print("5)Devolucion arriendo de un libro")
    print("6)salir")
    p=print("¿Que desea hacer?: ")
    r=input("--> ")
    if r=="1":
        f=name1.show_inventory(save1)
        print(f)
        filter=input("Desea filtrar por genero o autor(si/no): ")
        if filter=="si":
            filter1=input("escriba el genero o autor: ")
            filtro=name1.filter(save1,filter1)
            
    if r=="2":
        name_book=input("Nombre del libro: ")
        author_book=input("Autor del libro: ")
        gender_book=input("Genero del libro: ")
        serie_book=input("Numero de serie del libro: ")
        book1=Book(name_book,author_book,gender_book,serie_book)
        save1=copy.facts(book1)
    if r=="3":
        option=input("eliminar libro o ejemplar: ")
        if option=="libro":
            n=input("Nombre del libro para eliminar: ")
            delete=name1.delete_book(save1,n)
            save1=delete
        else:
            n=input("Nombre del libro: ")
            s=input("Numero de serie: ")
            delete=name1.delete_ejemplar(save1,n,s)
            save1=delete

    if r=="4":
        tipo=input("cliente o empleado: ")
        if tipo=="empleado":
            name=input("nombre persona: ")
            apellido=input("apellido: ")
            book=input("nombre libro a arrendar: ")
            name2=Employee(name,apellido)
            verifi=name2.checkout(save1,book)
            data=name2.save_rental(verifi,book)
            info=re.save(rent,name,data,book)
        else:
            name=input("nombre persona: ")
            apellido=input("apellido: ")
            book=input("nombre libro a arrendar: ")
            name2=Customer(name,apellido)
            verifi=name2.checkout(save1,book)
            data=name2.save_rental(verifi,book)
            info=re.save(rent,name,data,book)
    if r=="5":
        name=input("nombre de la persona que arrendo (solo nombre): ")
        r=re.mostrar(info,name)
        print(r)
        book=input("nombre del libro: ")
        devolucion=input("fecha devolucion (año/mes/dia): ")
        borrar=re.return_book(name,book,info)
        habi=name1.habilitado(save1,book)

    if r=="6":
        break

