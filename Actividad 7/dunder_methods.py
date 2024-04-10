from dataclasses import dataclass
from typing import List 

@dataclass
class Elemento:
    nombre = str

    def __eq__(self, other):
        return self.nombre == other.nombre
class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador


 #En Python, puedes definir una propiedad de solo lectura
 #utilizando el decorador *property* junto con métodos 
 #específicos para obtener y establecer el valor de la propiedad   
    @property
    def id(self):
        return self.__id
    
    def contiene(self, elemento: Elemento) -> bool:
        return any(e.nombre ==elemento.nombre for e in self.elementos)
    
    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)


#Para habilitar la operación de suma (+) entre dos instancias
#de la clase Conjunto, podemos sobrecargar el método especial
#(__add__). Este método especial nos permite definir 
#el comportamiento de la suma entre dos objetos de la clase.
    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
    def unir(self, otro_conjunto):
        return self + otro_conjunto
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
    def __str__(self):
        elemento_str = ', '.join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elemento_str})"
        