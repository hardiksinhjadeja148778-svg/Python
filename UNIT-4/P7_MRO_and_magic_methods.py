# Method Resolution Order (MRO)
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
print("MRO:", D.__mro__)
print("MRO names:", [cls.__name__ for cls in D.mro()])

# Magic methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return "Book: " + self.title

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python", 300)
b2 = Book("Java", 250)
print(b1)
print(len(b1))
print(b1 + b2)