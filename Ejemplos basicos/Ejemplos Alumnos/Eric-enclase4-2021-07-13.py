
def OpenFile(tcArchi, palabra):
    try:
        with open(tcArchi, mode="tr", encoding="utf8") as entrada:
                texto=entrada.read()
                return(texto.count(palabra))

    except :
        print(f"El archivo no existe")
    else:
        print("Hola")        
    finally:
        print("No importa qué pasó, esto se ejecuta igual")
      

print(OpenFile("quijote.txt", "en"))