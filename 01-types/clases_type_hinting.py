class Person:
    
    def __init__(self,name:str,position:int) -> None:
        self.name = name
        self.position = position
        
    def walk(self,distance_km:int) -> int:
        self.position += distance_km
        return self.position
    
paco = Person(name="Paco", position=0)
position_paco = paco.walk(distance_km=6)
print(position_paco)
