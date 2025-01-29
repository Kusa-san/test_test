class student:
#class properties
    gender =''
#
    def __init__(self, name, age):
        self.name = name
        self.age = age
#class meetods
    @classmethod
    def set_gender(cls):
        cls.gender='male'
        return cls.gender

    @staticmethod
    def is_adult(age):
        if age>18:
            print('Adult')
        else:
            print('probably a Minooooooooooor!!!!!')
#
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
#
kusa = student('kusa', 27)
print(kusa)
print(student.set_gender())
student.is_adult(18)