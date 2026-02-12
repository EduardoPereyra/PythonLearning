class Person:
    type = "human"
    
    def __init__(self, name:str, surname:str, age:int) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.identity_document = None
        
    def set_identity_document(self, identity_document:int) -> None:
        self.identity_document = identity_document
        print(f"Identity document set to: {self.identity_document}")
        
    def do_something(self) -> None: print("Doing something...")
    
    
    
class Athlete(Person):
    
    def __init__(self, name: str, surname: str, age: int, sport: str) -> None:
        super().__init__(name, surname, age)
        self.sport = sport
        
    def do_something(self) -> None:
        super().do_something()
        print(f"Playing {self.sport}")
        
class Cyclist(Athlete): 
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.sport = "Cycling"
        super().__init__(name, surname, age, self.sport) 
    
    def cycle(self) -> None: print("Cycling...")
        
        


juliana = Athlete("Juliana", "Silva", 26, "Tennis")
juliana.set_identity_document(123456)

print(juliana.sport)
juliana.do_something()

maria = Cyclist("Maria", "Gomes", 30)
maria.set_identity_document(654321)
maria.cycle()