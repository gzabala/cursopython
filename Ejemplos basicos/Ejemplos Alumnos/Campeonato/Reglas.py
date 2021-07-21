from abc import abstractmethod
from random import randint


class Reglas:
    def __init__(self, pg, pe, pp):
        self.__puntos_pg = pg
        self.__puntos_pe = pe
        self.__puntos_pp = pp
        
    @property
    def partido_ganado(self):
        return self.__puntos_pg
    @property
    def partido_empatado(self):
        return self.__puntos_pe
    @property
    def partido_perdido(self):
        return self.__puntos_pp

    @abstractmethod
    def marcador_aleatorio(self):
        pass
    
class Reglas_de_futbol(Reglas):
    def __init__(self):
        return super().__init__(3,1,0)

    def marcador_aleatorio(self):
        return randint(0,10)

class Reglas_de_badminton(Reglas):
    def __init__(self):
        return super().__init__(4,2,1)

    def marcador_aleatorio(self):
        return randint(0,21)

class Reglas_de_tenis(Reglas):
    def __init__(self):
        return super().__init__(1,0,0)

    def marcador_aleatorio(self):
        return randint(0,6)


