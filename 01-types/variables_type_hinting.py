from typing import List, Tuple, Dict


name: str
name = "Eduardo"

age:int = 25

pi:float = 3.1416

#surname:list[str] = ["Perez", "Doe", "Tafur"]
surname:List[str] = ["Perez", "Doe", "Tafur"]

#programming_languages: tuple[str,str,str,str]  = ("python", "java", "javascript", "golang")
programming_languages: Tuple[str,str,str,str] = ("python", "java", "javascript", "golang")

#language: dict[str,str] = {"nombre":"python", "creador":"Guido Van Rossum"}
language: Dict[str,str] = {"nombre":"python", "creador":"Guido Van Rossum"}