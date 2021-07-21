import funciones
import httplib2
#from googleapiclient.htt p import MediaIoBaseDownload
import io

equipos=funciones.levantarCsv('srvfinalv2.csv')
service=funciones.generaServicio()

# # Call the Drive v3 API
# results = service.files().list(
#     q="mimeType = 'application/vnd.google-apps.folder'",pageSize=200, fields="nextPageToken, files(id, name)").execute()
# items = results.get('files', [])

# if not items:
#     print('No files found.')
totalBajados=0
totalFallados=0
error=open("error.txt", "wt")
for equi in equipos:
    try:
        resultado=service.files().list(q="'"+equi+"' in parents and trashed=false", pageSize=1, fields="nextPageToken, files(id, name)", supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        if len(resultado['files'])==0:
            print(f"{equipos[equi]['nombre']} no tiene archivos en la carpeta")
            error.write(f"{equipos[equi]['nombre']} no tiene archivos en la carpeta\n")    
        else:
            data=resultado['files'][0]
            file_id = data['id']
            nombre="C:/srv/" + equipos[equi]['categoria'] + "/" + equipos[equi]['zona'] + "/" + equipos[equi]['nombre']
            #nombre="C:/srv/" + equipos[equi]['nombre']
            file=open( nombre, "wb")
            funciones.download_file(service, file_id, file, equipos[equi]['nombre'])
            file.close()
            print(f"PUDO bajar equipo de {equipos[equi]['nombre']}")
            totalBajados+=1
    except:
        print(f"No pudo bajar equipo de {equipos[equi]['nombre']}")
        error.write(f"No pudo bajar equipo de {equipos[equi]['nombre']}\n")
        totalFallados+=1
    
    # if totalBajados+totalFallados>1: #Para hacer una prueba con los primeros
    #     break
print(f"Total bajados: {totalBajados} - Total fallados: {totalFallados}")
error.close()