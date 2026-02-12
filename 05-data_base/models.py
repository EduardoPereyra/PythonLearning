from conexion import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String

class Department(BaseModel): 
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    def __init__(self, name:str): 
        self.name = name
    
    def __str__(self): return f"{self.id} {self.name}"
    
class Employee(BaseModel):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False) 
    
    def __init__(self, name:str, surname:str, document:str, department_id:Column[int]): 
        self.name = name 
        self.surname = surname
        self.document = document
        self.department_id = department_id
        
    def __str__(self):
        return f"{self.id} {self.name} {self.surname}"
    