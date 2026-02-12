class Persona:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        self.distance_made= 0
    
    def __add__(self, distance:int):
        self.distance_made += distance
        return self.distance_made
    
    def __lt__(self, other:"Persona"):
        return self.age < other.age

paco= Persona("Paco", 30)
emilio= Persona("Emilio", 25)

paco + 5
paco + 15
print(paco.distance_made)
print(paco < emilio)
print(paco > emilio)