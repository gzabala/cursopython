import requests
import json
from datetime import datetime, timedelta
 
pais= input("Ingrese país: ").lower().capitalize()
anio= input("Ingrese año (4 dig): ")
mes= input("Ingrese mes (2 dig): ")
feinicio = datetime.strptime(anio+'-'+mes+'-01', "%Y-%m-%d")
if int(mes) == 12:
    aniof=str(int(anio)+1)
    mesf='01'
else:
    mesf=str(int(mes)+1)
    aniof=anio
fefin=datetime.strptime(aniof+'-'+mesf+'-01', "%Y-%m-%d")+timedelta(days=-1)
url=f"https://api.covid19tracking.narrativa.com/api/country/{pais}?date_from={feinicio}&date_to={fefin}"
respuesta=requests.get(url)
if respuesta:
    resu=json.loads(respuesta.text)
    total=0
    for d in resu['dates']:
        total += resu['dates'][d]['countries'][pais]['today_new_confirmed']
    print(f'Cantidad de Personas contagiadas en {pais}: Periodo: {mes}/{anio} Total {total:0,.0f} personas')