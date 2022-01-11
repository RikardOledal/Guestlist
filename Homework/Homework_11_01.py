
'''Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another 
one called Teacher. Try to find as many methods and attributes as you 
can which belong to different classes, and keep in mind which are common 
and which are not. For example, the name should be a Person attribute, while 
salary should only be available to the teacher. '''

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"<Name: {self.name} Age: {self.age}"

class Student(Person):
    def __init__(self, name, course=None, age=18):
        '''name should be string\n
        course should be list\n
        age should be integer'''
        super().__init__(name, age=age)
        self.course = [] if course is None else course
    
    def add_course(self, new_course):
        '''new_course should be string'''
        self.course.append(new_course)
    
    def who_is(self):
        return f"{self.name} is a {self.age} year old Student that studies {self.course}"

class Teacher(Person):
    def __init__(self, name, salary=None, age=18):
        super().__init__(name, age=age)
        self.salary = [] if salary is None else salary

    def pay(self, payment):
        '''payment should be integer'''
        if type(payment) is not int:
            raise ValueError("Payment should be a interer")
        self.salary.append(payment)

    def total_salary(self):
        return sum(self.salary)
    
    def avarage_salary(self):
        return sum(self.salary)/len(self.salary)

louise = Student("Louise Oledal")
rikard = Teacher("Rikard Oledal")
louise.add_course("Matematik")
rikard.pay(10000)
rikard.pay(15000)
rikard.pay(12000)
rikard.pay(12000)
print(rikard.total_salary())
print(rikard.avarage_salary())
print(louise.who_is())
print(louise)


    
