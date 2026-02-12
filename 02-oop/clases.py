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
    
paco = Person("Paco", "Gomez", 30)
print(paco.name) # Output: Paco
paco.set_identity_document(12345678) # Output: Identity document set to: 12345678A
