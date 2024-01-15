class Person:
    def __init__(self,fName,lName):
        self.fName=fName
        self.lName=lName
    def printDetails(self):
        print('The name of the person is '+self.fName)


class Student(Person):
    def __init__(self,fName,lName,year):
        Person.__init__(self,fName,lName)#passing the parameters to the parent class
        self.gradyear=year
    def welcome(self):
        print(f"Hello {self.fName} {self.lName} we welcome you to {self.gradyear} Btech batch")


class Teacher(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)#passing the parameters to the parent class 2nd method


student=Student("vishwa","appaji",2025)
student.printDetails()
student.welcome()