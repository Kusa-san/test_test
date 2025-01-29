class boy:
#
    #class property
    number_of_instances = 0
#
    #properties
#
    def __init__(self,name,year,grades):
        self.name=name
        self.year=year
        self.grades=grades
#
    #methods
#
    def info(self):
        print(f"Student Name is {self.name} and in year {self.year} with grade {self.grade}")
#    
    def __str__(self):
        return f"Student Name is {self.name} and in year {self.year} with grade {self.grade}"
#
    def GPA(self):
        for i in range (len(self.grades)):
            if self.grades[i] >= 90:
                print(f"{self.name} have A+")
            elif self.grades[i] >= 80:
                print(f"{self.name} have A")
            elif self.grades[i] >= 70:
                print(f"{self.name} have B")
            elif self.grades[i] >= 60:
                print(f"{self.name} have C")
            elif self.grades[i] >= 50:
                print(f"{self.name} have D")
            else:
                print(f"{self.name} have F")
#
    def introduction(self):
        print(f"Hi this is {self.name},I'm at the {self.year} year, and i scored {self.grades}")
#
    def __str__(self):
        return f"{self.name} is in the  {self.year}-th year"
#
kusa = boy('Kusa', 4,[55,90,41])
ali = boy('Ali Hassan', 4,[68,74,55])
kusa.introduction()
ali.introduction()
print(ali)
print(kusa)
ali.GPA()

