# Quiero representar el personal de una escuela. 
# Tengo administrativos, directivos, docentes y alumnos. PEnsar qué tienen en común, qué diferente y hacer una implementación sencilla de Personal.
from datetime import date

class Persona():
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento    

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido=apellido

    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_de_nacimiento):
        self.__fecha_de_nacimiento=fecha_de_nacimiento

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Fecha de Nacimiento: {self.fecha_de_nacimiento}"