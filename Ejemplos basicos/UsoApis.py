import requests
import json
nombre=input("Ingrese el nombre deseado: ")
conversionSexo={"male":"masculino", "female":"femenino"}

url="https://api.agify.io"
argum={"name": nombre}
resp=requests.get(url, params=argum)
if resp:
    # print(resp.text)
    dict=resp.json()
    edad=dict["age"]

url="https://api.genderize.io"
resp=requests.get(url, params=argum)
if resp:
    # print(resp.text)
    dict=resp.json()
    sexo=conversionSexo[dict["gender"]]
    probabilidad=dict["probability"]

url="https://api.nationalize.io"
resp=requests.get(url, params=argum)
if resp:
    # print(resp.text)
    dict=resp.json()
    codpais=dict["country"][0]["country_id"]
    probabPais=round(dict["country"][0]["probability"],2)

# Así obtengo el país
url="https://restcountries.eu/rest/v2/alpha/"+codpais
resp=requests.get(url)
if resp:
    # print(resp.text)
    dict=resp.json()
    pais=dict["name"]


print(f"{nombre} es un nombre {sexo} con una probabilidad de {probabilidad}. La edad promedio de las personas con ese nombre es de {edad}. Y hay una probabilidad de {probabpais} de que sea de {pais}")


