from Ejercicios_de_archivos import file3 

# archivo="Contenido\Ejemplosbasicos\quijote.txt"
archivo=input("Ingrese el nombre del archivo con el path completo:")
palabra=input("Ingrese la palabra a buscar: ")


# try:
#     resultado=file3(archivo, palabra)
# except FileNotFoundError:
#     print("El archivo no existe")
# else:
#     print(f"La cantidad de veces que aparece {palabra} en {archivo} es {resultado}")

assert len(archivo)>0, "Debe existir un nombre de archivo"
assert len(palabra)>0, "La palabra a buscar debe tener por lo menos un caracter"
try:
    resultado=file3(archivo, palabra)
    assert resultado>=0, "No puede haber encontrado la palabra un número negativo de veces"
except FileNotFoundError:
    print("El archivo no existe")
else:
    print(f"La cantidad de veces que aparece {palabra} en {archivo} es {resultado}")

    
