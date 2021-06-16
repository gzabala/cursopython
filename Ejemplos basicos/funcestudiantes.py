
def lista(txt):

    i=0

    l=len(txt)
    lisdev=[]
    while i<l:

        if len(txt[i:i+2])<2:

            lisdev.append(txt[i:i+2]+"_")

        else:

            lisdev.append(txt[i:i+2])

        i=i+2
    return lisdev

# a="algun perr"
# print(lista(a))

def dividirdeados(cadena):
    lista=list()
    # if len(cadena)%2!=0 :cadena.append("_")
    for i in range(0,len(cadena)-1,2):
        lista.append(cadena[i:i+2])
    if len(cadena)%2!=0 :lista.append(cadena[-1]+"_")    
    return lista 

# print(dividirdeados("Un ejemplo"))
# print(dividirdeados("Este es un ejemplo"))
# print(dividirdeados("Un ejemplar"))

def fun1Recursivo(param):
    if len(param)<=2:
        return [(param+"_")[:2]]
    else:
        return [param[:2]]+fun1Recursivo(param[2:])

# print(fun1Recursivo("Un ejemplo"))
# print(fun1Recursivo("Este es un ejemplo"))
# print(fun1Recursivo("Un ejemplar"))

def imprimeDeADos(cadena):
    lista = []
    for i in range(0, len(cadena), 2):
        lista.append(cadena[i:i+2].ljust(2, "_"))
        
    return lista
    
cadena = "esta es una caden"
print(imprimeDeADos(cadena))
