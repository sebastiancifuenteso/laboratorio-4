

class Bookcopy():
    def __init__(self,data):
        self.data=data

    def facts(self,book):
        dicc={}
        data1=book.save()
        if data1[0]in self.data:
            self.data[data1[0]]["estado"].append("disponible")
            self.data[data1[0]]["numero de serie"].append(data1[3])
        else:
            dicc["autor"]=data1[1]
            dicc["genero"]=data1[2]
            dicc["estado"]=["disponible"]
            dicc["numero de serie"]=[data1[3]]
            self.data[data1[0]]=dicc
        return self.data


