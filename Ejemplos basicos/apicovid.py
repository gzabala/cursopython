import requests
import json
pais=input("Ingrese país: ")
anio=input("Ingrese año (4 dig): ")
mes=input("Ingrese mes (2 dig): ")
url=f"https://api.covid19tracking.narrativa.com/api/country/{pais}?date_from={anio}-{mes}-01&date_to={anio}-{mes}-30"
resp=requests.get(url)


if resp:
    print("---")
    resu=json.loads(resp.text)
    print(resu)
    