from datetime import date
from random import randint
import Equipo
import Reglas

class Partido:
    def __init__(self, equipo1, equipo2):
        self.__fecha = date.today()
        self.__equipo1 = equipo1
        self.__equipo2 = equipo2
        self.__marcador_equipo1=0
        self.__marcador_equipo2=0
        self.__estado = "No Jugado"

    @property
    def equipo1(self):
        return self.__equipo1

    @property
    def equipo2(self):
        return self.__equipo2

    @property
    def marcador_equipo1(self):
        return self.__marcador_equipo1

    @property
    def marcador_equipo2(self):
        return self.__marcador_equipo2

    def __str__(self):
        if self.__estado == "No Jugado":
            return f"Partido no jugado aun entre {self.equipo1} y {self.equipo2}"
        else:
            if self.marcador_equipo1>self.marcador_equipo2:
                return f"Ganador {self.equipo1} sobre {self.equipo2} - {self.marcador_equipo1} a {self.marcador_equipo2}"
            elif self.marcador_equipo1 < self.marcador_equipo2:
                return f"Ganador {self.equipo2} sobre {self.equipo1} - {self.marcador_equipo2} a {self.marcador_equipo1}"
            else:
                return f"Empate entre {self.equipo1} y {self.equipo2} - {self.marcador_equipo1} a {self.marcador_equipo2}"
    
    def asignar_marcadores(self):
        self.equipo1.agregarGolesaFavor(self.marcador_equipo1)
        self.equipo1.agregarGolesenContra(self.marcador_equipo2)
        self.equipo2.agregarGolesaFavor(self.marcador_equipo2)
        self.equipo2.agregarGolesenContra(self.marcador_equipo1)

    def gano_equipo1(self, reglas):
        self.equipo1.partido_ganado()
        self.equipo2.partido_perdido()
        self.equipo1.agregar_puntos(reglas.partido_ganado)
        self.equipo2.agregar_puntos(reglas.partido_perdido)

    def gano_equipo2(self, reglas):
        self.equipo2.partido_ganado()
        self.equipo1.partido_perdido()
        self.equipo2.agregar_puntos(reglas.partido_ganado)
        self.equipo1.agregar_puntos(reglas.partido_perdido)

    def empate(self, reglas):
        self.equipo1.partido_empatado()
        self.equipo2.partido_empatado()
        self.equipo1.agregar_puntos(reglas.partido_empatado)
        self.equipo2.agregar_puntos(reglas.partido_empatado)    
    
    def jugar(self, reglas):
        self.__marcador_equipo1 = reglas.marcador_aleatorio()
        self.__marcador_equipo2 = reglas.marcador_aleatorio()
        self.__estado = "Jugado"
        self.asignar_marcadores()
        if self.marcador_equipo1 > self.marcador_equipo2:
            self.gano_equipo1(reglas)
        elif self.marcador_equipo1 < self.marcador_equipo2:
            self.gano_equipo2(reglas)
        else:
            self.empate(reglas)





