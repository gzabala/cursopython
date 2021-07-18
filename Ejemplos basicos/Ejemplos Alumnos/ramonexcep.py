def leer_palabras(archi, pal):
    count_palabras = 0
    if archi == "" or len(archi) == 0 :
        raise Exception("El nombre de archivo no puede ser vacio")
    if pal == "":
        raise Exception("la palabra no debe ser vacia")
    try: 
        with open(archi, mode="tr", encoding="utf8") as entrada:
            texto=entrada.read()
            palabras=texto.split()
            count_palabras = palabras.count(pal)
    except:
        count_palabras = 0
    finally:
        return count_palabras

ar=input("Ingrese archivo: ")
pal=input("Ingrese palabra: ")
resu=""
try:
    resu=leer_palabras(ar, pal)
except Exception as exc:
    print(f"El archivo o la palabra a buscar estaban vacíos, el error fue {exc}")

print(resu)
