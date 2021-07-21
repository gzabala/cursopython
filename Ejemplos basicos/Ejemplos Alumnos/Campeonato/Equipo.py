# Se desea implementar un framework para campeonatos de diversas disciplinas. 
# Para eso se ha decidido la creación de dos clases (decidir si son abstractas o no) que permitan definir los elementos esenciales del framework, 
# y que luego heredadas permitan la creación de diferentes campeonatos.  

# Equipo: representa a un equipo participante del campeonato. Debe conocer los partidos que ha ganado, perdido y empatado. 
# Debe poder responder cuántos puntos tiene, en qué posición se encuentra y si por ahora desciende o no (está entre los últimos dos equipos)
  
# Campeonato: representa a un campeonato compuesto por varios equipos. 
# Debe conocer el año en el que se desarrolla el campeonato, los puntos que entrega por cada partido ganado, empatado o perdido respectivamente. 
# Debe poder responder con la tabla de posiciones y la cantidad de equipos que tiene en el campeonato.  
# Por otra parte, deseamos modelar campeonatos de fútbol, donde se da 3 puntos por pg y 1 por pe.
# Campeonatos de badminton, donde se da 4 puntos por pg, 2 por pe, y 1 por pp.  

# Los equipos de fútbol además deben conocer la cantidad de goles a favor y goles en contra. 
# Deben poder responder cuál es la diferencia de goles. Los campeonatos de fútbol también deben poder responder cuando se le solicita la cantidad total de goles del campeonato.  

from Persona.Persona import Persona

class Equipo:
    def __init__(self, nombre, miembros):
        self.__nombre = nombre
        self.__miembros=miembros
        self.__puntos=0
        self.__partidos_ganados = 0
        self.__partidos_empatados = 0
        self.__partidos_perdidos = 0
        self.__marcador_a_favor = 0
        self.__marcador_en_contra = 0

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self, puntos):
        self.__puntos=puntos
    
    def agregar_puntos(self,puntos):
        self.__puntos += puntos

    @property
    def miembros(self):
        return self.__miembros

    @property
    def partidos_ganados(self):
        return self.__partidos_ganados

    @property
    def partidos_empatados(self):
        return self.__partidos_empatados

    @property
    def partidos_perdidos(self):
        return self.__partidos_perdidos

    @property
    def goles_a_favor(self):
        return self.__marcador_a_favor

    @property
    def goles_en_contra(self):
        return self.__marcador_en_contra

    @property
    def diferencia_de_gol(self):
        return self.__marcador_a_favor - self.__marcador_en_contra

    def agregarGolesaFavor(self, goles):
        self.__marcador_a_favor += goles

    def agregarGolesenContra(self, goles):
        self.__marcador_en_contra += goles
    
    def partido_ganado(self):
        self.__partidos_ganados+=1

    def partido_empatado(self):
        self.__partidos_empatados+=1

    def partido_perdido(self):
        self.__partidos_perdidos+=1

    def agregarMiembro(self, persona):
        self.__miembros.append(persona)

    def eliminarMiembro(self, persona):
        self.__miembros.remove(persona)

    def listarMiembros(self):
        print(f"miembros del equipo {self.nombre}")
        print(f"Total: {len(self.__miembros)}")
        for per in self.__miembros:
            print(per)

    def __lt__(self, other):
        return (self.puntos < other.puntos) or (self.puntos == other.puntos and self.partidos_ganados < other.partidos_ganados) or (self.puntos == other.puntos and self.partidos_ganados == other.partidos_ganados and self.diferencia_de_gol < other.diferencia_de_gol)

    def __eq__(self, other):
        return (self.putnos == other.puntos and self.partidos_ganados == other.partidos_ganados and self.diferencia_de_gol == self.diferencia_de_gol)

    def __str__(self):
        return self.__nombre