class Student:
#
    #properties
    number_of_instances = 0
    info="This is a class for Students"
#
    def __init__(self,name,year,grades):
        self.name=name
        self.year=year
        self.grades=grades
#
@classmethod
def class_info(cls):
    print(Student.info)
#
    #methods
#
    def introduction(self):
        print(f"Hi this is {self.name},I'm at the {self.year} year, and i scored {self.grades}")
#    
    def __str__(self):
        return f"{self.name} have {self.year} year"
#
me = Student('Ali Hassan', 4,[20,3,55])
x = Student('X', 4,[55,9,0])
ali = Student('not Ali', 4,[66,87,99])
#
print(Student.number_of_instances)
Student.class_info()
me.introduction()
x.introduction()