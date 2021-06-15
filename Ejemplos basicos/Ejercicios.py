print("Ejercicios")

# Ejercicio 1
# numero = input("Ingrese un número: ")
# print(type(numero))
# print(len(str(numero)))

# Ejercicio 2
# cadena="la casa de al lado"
# cadena="Ahora, que nos hemos separado"
# print(cadena.split()[0])

# cadena="Holaasdasdad como va"
# i=0
# for l in cadena:
#     if l == " ": 
#         print("Palabra: ", cadena[:i]) 
#         break                   
#     i+=1


# lcCadena="Debe estar en America del sur bien al sur"
# espacio=lcCadena.index(" ")
# print(espacio)
# print(lcCadena[:espacio])

# lista=  [4, 8, 3, 2, 3, 7, 5] 
# elem= 14
# posi=lista.index(elem)
# print(lista[posi:])

numero=763865900
lista=list(str(numero))
print(lista)
i=len(lista)-1
while(lista[i]=="0"):
    print(lista[i])
    i-=1
    