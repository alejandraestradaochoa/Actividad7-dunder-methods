from dataclasses import dataclass
from typing import List 

@dataclass(eq=True, frozen=True)
class Elemento:
    nombre = str

class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    def id(self):
        return self.__id
    
    def contiene(self, elemento: Elemento) -> bool:
        return any(e.nombre ==elemento.nombre for e in self.elementos)
    