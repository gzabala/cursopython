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
from datetime import date
from Equipo import Equipo
from Partido import Partido
import Reglas

class Campeonato:
    def __init__(self, año, nombre, reglas):
        self.__year= año
        self.__nombre = nombre
        self.__reglas = reglas
        self.__partidos = []
        self.__equipos = []
    
    @property
    def año(self):
        return self.__year

    @property
    def nombre(self):
        return self.__nombre

    @property
    def reglas(self):
        return self.__reglas

    @property
    def partidos(self):
        return self.__partidos

    @property
    def equipos(self):
        return self.__equipos

    def agregarEquipo(self, equipo):
        self.__equipos.append(equipo)

    def eliminarEquipo(self, equipo):
        self.__equipos.remove(equipo)

    def generar_fixture(self):
        self.__partidos = [Partido(eq1,eq2) for eq1 in self.__equipos for eq2 in self.__equipos if eq1.nombre < eq2.nombre]

    def listar_partidos(self):
        for partido in self.__partidos:
            print(partido)
    
    def jugar(self):
        for partido in self.__partidos:
            partido.jugar(self.__reglas)

    def tabla_de_posiciones(self):
        self.equipos.sort(reverse=True)
        return self.equipos        
    
    def desciende(self,cantidad_de_equipos):
        self.tabla_de_posiciones()
        desc = self.equipos
        desc.reverse()
        return desc[:cantidad_de_equipos:]




    



        

