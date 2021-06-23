
# def lista(txt):

#     i=0

#     l=len(txt)
#     lisdev=[]
#     while i<l:

#         if len(txt[i:i+2])<2:

#             lisdev.append(txt[i:i+2]+"_")

#         else:

#             lisdev.append(txt[i:i+2])

#         i=i+2
#     return lisdev

# a="algun perr"
# print(lista(a))

# def dividirdeados(cadena):
#     lista=list()
#     # if len(cadena)%2!=0 :cadena.append("_")
#     for i in range(0,len(cadena)-1,2):
#         lista.append(cadena[i:i+2])
#     if len(cadena)%2!=0 :lista.append(cadena[-1]+"_")    
#     return lista 

# print(dividirdeados("Un ejemplo"))
# print(dividirdeados("Este es un ejemplo"))
# print(dividirdeados("Un ejemplar"))

# def fun1Recursivo(param):
#     if len(param)<=2:
#         return [(param+"_")[:2]]
#     else:
#         return [param[:2]]+fun1Recursivo(param[2:])

# print(fun1Recursivo("Un ejemplo"))
# print(fun1Recursivo("Este es un ejemplo"))
# print(fun1Recursivo("Un ejemplar"))

# def imprimeDeADos(cadena):
#     lista = []
#     for i in range(0, len(cadena), 2):
#         lista.append(cadena[i:i+2].ljust(2, "_"))
        
#     return lista
    
# cadena = "esta es una caden"
# print(imprimeDeADos(cadena))

def cantidad_de_puntos_al_inicio(cadena):
    i=0
    while(cadena[i]=="."):
        i+=1
    return i

# print(cantidad_de_puntos_al_inicio(".....casa"))

cadena=".....casa"

def puntos(cadena):
    largo=0
    for i in cadena:
        if i == '.':
            largo+=1
        else:
            break
    return largo

# print(puntos(".....casa"))

def cantidad_puntos_al_inicio(cadena):
    count_puntos = 0
    for item in cadena:
        if item == "." :
            count_puntos += 1
        else:
            return count_puntos

# print(cantidad_puntos_al_inicio(".....casa"))  

# def contarPuntos(cadena):
#     i=0
#     i=cadena.count(".")
#     return i

# cadena="...c...adena"
# cantidadDePuntos=contarPuntos(cadena)
# print("Cantidad de Puntos: ", cantidadDePuntos)

def devolverNumCercano(conjunto,numero):
    i=0
    listaValor=[]
    listaResu=[]
    for d in conjunto:
        res=abs(numero-d)
        if (res)>=0:
            listaValor.append(d)
            listaResu.append(res)
        else:
             return d
    i+=1
    valorMinimo=min(listaResu)
    indiceDelMinimo=listaResu.index(valorMinimo)
    valorCercano=listaValor[indiceDelMinimo]
    return valorCercano



# conj1=[12,108, 232,33422,34,5,56]
# conj1=[140, 130, 120]

# valor=109

# valorCercano=devolverNumCercano(conj1,valor)

# print("Valor Cercano: ",valorCercano)

def invierte_cadena(cadena):
    #salida=[str(item) for item in cadena[::-1]]
    salida = "".join([str(item) for item in cadena[::-1]])
    return salida

# print(invierte_cadena("asdfg hjkl"))
# print("asdfg hjkl"[::-1])

def invertir_palabras(cadena):
    cadenainvertida =""
    for palabra in cadena.split():
        cadenainvertida = cadenainvertida + " " + palabra[::-1]
    return cadenainvertida.strip()

cadena="Esto es un ejemplo"
print(invertir_palabras(cadena))
