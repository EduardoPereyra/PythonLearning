class employee:
    def __init__(self, name: str, surname: str, salary: float):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.working_hours = 0
        
    def work(self, hours:int):
        self.working_hours += hours
        print(f"{self.name} {self.surname} has worked for {hours} hours. Total working hours: {self.working_hours}")

    def get_salary(self): 
        print(f"{self.name} {self.surname} has a salary of {self.salary}")