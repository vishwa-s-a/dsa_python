class myClass:
    x=5
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"My name is {self.name} and {self.age} years old"
    def greet(self):#one argument is fixed for every method that is self
        print('Hello, Gracias Tu hablas espanol')



object = myClass('John',23)
print(object.greet())
print(object.name)
print(object)

object.age=32#modifing the objects
print(object)
del object
print(object)
