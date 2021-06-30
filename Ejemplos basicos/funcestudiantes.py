
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

# cadena="Esto es un ejemplo"
# print(invertir_palabras(cadena))


def contarDigitos(cadena):
    digitos=0
    for i in cadena:
        if i.isdigit():
            digitos+=1
    return digitos

def cantidad_de_digitos(cadena):
    cantidaddedigitos=0
    for palabra in cadena.split():
        if palabra.isnumeric():
            cantidaddedigitos+=len(palabra)
    return cantidaddedigitos

# print(contarDigitos("Acá tenemos 223 dígi333to00s"))
# print(cantidad_de_digitos("Acá tenemos 223 dígi333to00s"))

def encontrar_caros(cantidad, *lista):
    listaordenada = sorted(lista, key=lambda i: i["pre"], reverse=True)
    return listaordenada[:cantidad]
    
 
# print(encontrar_caros(2,{"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}))
# print(encontrar_caros(5,[{"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}]))
# print(encontrar_caros(1,[{"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}]))
# print(encontrar_caros(0,[{"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}]))


def segundaOcurrencia(c1, c2):
    import re
    l2= [m.start() for m in re.finditer(c2, c1)]
    if (len(l2)>=2):
         return (l2[1])
    else:
         return None

# s1 = 'Esta es una frase que queremos encontrar'
# s2 = 'que'
# print(segundaOcurrencia(s1,s2))

def busco_cadena(cadena1,cadena2):
    if cadena1.count(cadena2) <= 1:
        retorno="None"
    else:
        indice=cadena1.find(cadena2)+1
        retorno=cadena1.find(cadena2,indice)
    return retorno

# print(busco_cadena("Esto es una estatua", "st"))
s1 = 'Esta es una frase que queremos encontrar'
s2 = 'que'
print(busco_cadena(s1,s2))
