class Employee:
    # Class property
    all_employees = []

    # Constructor
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.all_employees.append(self)

    # Instance Methods
    def promote(self, new_salary):
        self.salary = new_salary

    def transfer(self, new_department):
        self.department = new_department

    @classmethod
    def get_employees_by_department(cls, department):
        department_employees = []
        for i in cls.all_employees:
            if i.department == department:
                department_employees.append(str(i))
        return department_employees
    
    @classmethod
    def get_employees_by_salary(cls, salary):
        department_salary = []
        for i in cls.all_employees:
            if i.salary >= salary:
                department_salary.append(str(i))
        return department_salary

    def __str__(self):
        return f"{self.name} from {self.department}"

# Example Usage:
employee1 = Employee("Alice", 50000, "HR")
employee2 = Employee("Bob", 60000, "Finance")
employee3 = Employee("Mohamad", 40000, "Tech")
employee4 = Employee("Sam", 55000, "Finance")
employee5 = Employee("Mik", 45000, "Tech")
employee6 = Employee("Monica", 65000, "HR")
hr_employees = Employee.get_employees_by_department("HR")
print(hr_employees)  # Output: ['Alice']
salary_employees = Employee.get_employees_by_salary(50000)
print(salary_employees)