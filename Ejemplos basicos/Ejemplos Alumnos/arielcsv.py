import pandas as pd
import datetime as dt
 
# Opcion 1
df = pd.read_csv("owid-covid-data.csv", sep=',')
# print(df)
print(df['location'])
pais=(input('Ingrese Pais:')).lower().capitalize()
anio=int(input('Ingrese año : '))
mes=int(input('Ingrese mes: '))
a=df.loc[(df['location'] == pais) & (pd.to_datetime(df['date']).dt.year == anio) & (pd.to_datetime(df['date']).dt.month == mes) ,'new_cases'].sum()
print(f'Cantidad de Personas contagiadas en {pais}: Periodo: {mes}/{anio} Total {a:.0f} personas')