import requests
 
nombre = input("ingrese Nombre: ")
argum={"name":nombre}
url_age = "https://api.agify.io/"
url_gen = "https://api.genderize.io/"
url_nac = "https://api.nationalize.io/"
resp_age = requests.get(url_age, params=argum)
resp_gen = requests.get(url_gen, params=argum)
resp_nac = requests.get(url_nac, params=argum)
dic_age = resp_age.json()
dic_gen = resp_gen.json()
dic_nac = resp_nac.json()
# print(dic_age)
# print(dic_gen)
# print(dic_nac)
nac=dic_nac['country'][1]['country_id']

url="https://restcountries.eu/rest/v2/alpha/"+nac
resp=requests.get(url)
if resp:
    dict=resp.json()
    pais=dict["name"]

print(f"El nombre {nombre} precide edad {dic_age['age']} genero {dic_gen['gender']} nacionalidad {pais}")
