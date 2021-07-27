import requests
import json

# Calidad del aire Bahía blanca

# url="https://gobiernoabierto.bahia.gob.ar/WS/3042"
# resp=requests.get(url)
# if resp:
#     dicc=resp.json()
#     for ind in range(0,3):
#         print(f"El indicador {dicc[ind]['indicador']} tiene un valor de {dicc[ind]['valor']}")

print("-----------")

client_id="d020eaa6cb044625b0e3efc7244d2e7f"
client_secret="688c168E273b4d11Ae7E414131062dA0"

# Averiguar nro de estacion de la que está en el C3

url="https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationInformation"
data={"client_id":client_id, "client_secret":client_secret}
resp=requests.get(url, params=data)
if resp:
    dicc=resp.json()
    for estacion in dicc['data']['stations']:
        if "Oro" in estacion['address']:
            direccion=estacion['address']
            nroEstacion=estacion['station_id']
            break

url="https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus"
resp=requests.get(url, params=data)

if resp:
    dicc=resp.json()
    for estacion in dicc['data']['stations']:
        if estacion['station_id']==nroEstacion:
            print(f"La cantidad de bicicletas disponibles en la estación de {direccion} es {estacion['num_bikes_available']}")

