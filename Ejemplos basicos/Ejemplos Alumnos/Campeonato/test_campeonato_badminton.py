from datetime import date
from Campeonato import Campeonato
from Reglas import Reglas_de_badminton
from Equipo import Equipo
from Persona.Persona import Persona

eq1 = Equipo("Quilmes", [Persona("Jose","Jaramillo",date(1980,5,6)),Persona("Juan","Jaramillo",date(1986,7,22))])
eq2 = Equipo("Ezpeleta", [Persona("Daniel","Damasco",date(1980,5,6)),Persona("Diego","Damasco",date(1986,7,22))])
eq3 = Equipo("Sanrandi", [Persona("Esteban","Ergullo",date(1980,5,6)),Persona("Ernesto","Ergullo",date(1986,7,22))])
eq4 = Equipo("Berazategui", [Persona("Federico","Fernandez",date(1980,5,6)),Persona("Fernando","Fernandez",date(1986,7,22))])

# print(eq1)
# eq1.listarMiembros()
# print(eq2)
# eq2.listarMiembros()
# print(eq3)
# eq3.listarMiembros()
# print(eq4)
# eq4.listarMiembros()

c1 = Campeonato(2021,"badminton",Reglas_de_badminton())
c1.agregarEquipo(eq1)
c1.agregarEquipo(eq2)
c1.agregarEquipo(eq3)
c1.agregarEquipo(eq4)
c1.generar_fixture()

c1.jugar()

for par in c1.partidos:
    print(par)
print("------------------")

for eq in c1.tabla_de_posiciones():
    print(f"Equipo {eq.nombre} Puntos {eq.puntos} pg {eq.partidos_ganados} pe {eq.partidos_empatados} pp {eq.partidos_perdidos} gf {eq.goles_a_favor} gc {eq.goles_en_contra}")

for eq in c1.desciende(2):
    print(eq)





