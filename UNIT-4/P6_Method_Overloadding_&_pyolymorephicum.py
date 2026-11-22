# Method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):                    # overrides parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
a.sound()
Dog().sound()
Cat().sound()

# Polymorphism: same method name, different behaviour
print("--- Polymorphism ---")
for animal in [Animal(), Dog(), Cat()]:
    animal.sound()