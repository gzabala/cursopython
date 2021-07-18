## Excepciones
# 1. Modificar el programa que dado el nombre de un archivo y una palabra, devuelve la cantidad de apariciones de la palabra en el archivo, 
# para que pueda manejar excepciones como la inexistencia del archivo solicitado.
def cantidad_de_apariciones(archivo, palabra):
    with open(archivo, encoding="utf8") as archi:
        return archi.read().count(palabra)

arch = input("Nombre del archivo: ")
pal = input("Palabra a contar: ")

try:
    print(f"La palabra {pal} aparece {cantidad_de_apariciones(arch,pal)} en el archivo {arch}")
except FileNotFoundError:
    print("Archivo no existente")
        
# 2. Encapsular la funcionalidad anterior en una función, testeando la precondición que debe haber un nombre de archivo y una palabra antes de llamar a la función, y que debe devolver un resultado mayor o igual a cero posteriormente.



# Dado el nombre de un archivo y una palabra, devolver cuántas veces aparece la palabra en el archivo (como palabra, no como cadena)

# print(cantidad_de_apariciones("quijote.txt","hidalgo"))        
# print(cantidad_de_apariciones("quijote.txt","Quijote")) 
# print(cantidad_de_apariciones("quijote.txt","de")) 
# print(cantidad_de_apariciones("quijote.txt","Diego")) 

