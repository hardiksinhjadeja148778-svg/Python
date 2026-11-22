# Single inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Multilevel inheritance
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Multiple inheritance
class Father:
    def skill1(self):
        print("Father: Driving")

class Mother:
    def skill2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child: Programming")

print("--- Single ---")
d = Dog()
d.eat()
d.bark()

print("--- Multilevel ---")
p = Puppy()
p.eat()
p.bark()
p.weep()

print("--- Multiple ---")
c = Child()
c.skill1()
c.skill2()
c.skill3()