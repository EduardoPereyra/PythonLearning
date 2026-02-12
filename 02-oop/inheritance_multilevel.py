class FlyAnimal: 
    def eat(self): print("FlyAnimal can eat")
    def fly(self): print("I can fly")
    
class SwimAnimal:
    def eat(self): print("SwimAnimal can eat")
    def swim(self): print("I can swim")

class WalkingAnimal: 
    def eat(self): print("WalkingAnimal can eat")
    def walk(self): print("I can walk")
    
    
class Duck(FlyAnimal, SwimAnimal, WalkingAnimal):
    def quack(self): print("Quack!")
    
    
    
donald = Duck()
donald.eat()
donald.fly() 
donald.swim() 
donald.walk() 
donald.quack()