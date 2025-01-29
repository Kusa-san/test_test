class company:
#
    #properties
    number_of_instances = 0
    info_of_dep=[]
#
    def __init__(self,name,dep,sal):
        self.name=name
        self.dep=dep
        self.sal=sal
        company.number_of_instances += 1
        company.info_of_dep.append(dep)
#
    #methods
#
    @classmethod
    def class_info(cls):
        return(company.info_of_dep)
#
    def introduction(self):
        print(f"Hi this is {self.name} ,I'm at the {self.dep} dep, and i have {self.sal} k salary")
#    
    def __str__(self):
        return f"{self.name} have {self.dep} dep"
#
Ali = company('Ali Hassan','Front End', 20)
Kusa = company('Kusa','Moblie Dev',30)
jj = company('jj','Back End', 55)
#
print(f"there are {company.number_of_instances} instances of the class company")
Ali.introduction()
Kusa.introduction()
jj.introduction()
List=(company.class_info())
print(List)