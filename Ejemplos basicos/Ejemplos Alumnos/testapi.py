import requests

lcNombre=input("Ingrese Nombre: ")


#Age
url="https://api.agify.io?name="+lcNombre
print(url)
resp=requests.get(url)
if resp:
        dict=resp.json()
        print(f"Todo el diccionario: {dict}")


#Genero
url="https://api.genderize.io?name="+lcNombre
print(url)
resp=requests.get(url)
if resp:
        dict=resp.json()
        print(f"Todo el diccionario: {dict}")


#nationality 
url="https://api.nationalize.io?name="+lcNombre
print(url)
resp=requests.get(url)
if resp:
        dict=resp.json()
        print(f"Todo el diccionario: {dict}")

        

