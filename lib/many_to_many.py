class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return list({c.author for c in self.contracts()})


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be str")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be int")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]


a1 = Author("John")
a2 = Author("Jane")

b1 = Book("AI Systems")
b2 = Book("Deep Learning")

a1.sign_contract(b1, "2026-01-01", 500)
a1.sign_contract(b2, "2026-02-01", 300)
a2.sign_contract(b1, "2026-01-01", 700)

print(a1.books())             # [b1, b2]
print(b1.authors())           # [a1, a2]
print(a1.total_royalties())   # 800
print(Contract.contracts_by_date("2026-01-01"))