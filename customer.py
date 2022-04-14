class Customer (Person):
    def __init__(self, name, last_name, age):
        super().__init__(name, last_name, age)
    def checkout(self, book):
        super().checkout(book)
        self.leased_books.append(book)