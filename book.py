
class Book():
    def __init__(self,name,author,gender,serie):
        self.name=name
        self.author=author
        self.gender=gender
        self.serie=serie

    def save(self):
        return [self.name,self.author,self.gender,self.serie]

