###Ejercicio para BD
from datetime import date, datetime
import dbfread
    

def connect(tcType):
    if (tcType.upper()=="SQLITE"):
      import sqlite3
      from sqlite3.dbapi2 import Date
      try:
        conexion = sqlite3.connect('personal.db')
        #cursor = conexion.cursor()
      except (Exception, sqlite3.DatabaseError) as error:
        print(error)
      finally:
        return(conexion)
    elif (tcType.upper()=="PSQL"):
      import psycopg2
      try:
        conexion = psycopg2.connect(user = "postgres",
                                  password = "laclavedelexito",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")
      except (Exception, psycopg2.DatabaseError) as error:
        print(error)
      finally:
        return(conexion)
    elif (tcType.upper()=="MSSQL"):
      import pyodbc
      try:
        conexion =  pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=desarrollo2\sqlexpress;Database=PERSONAL;uid=sa;pwd=laclavedelexito")
      except (Exception, pyodbc.DatabaseError) as error:
        print(error)
      finally:
        return(conexion)
    elif(tcType.upper()=="DBF"):
      import dbfpy
      try:
        conexion =  ""
      except (Exception, dbfpy.DatabaseError) as error:
        print(error)
      finally:
        return(conexion)
    elif(tcType.upper()=="MONGO"):
      import pymongo
      try:
        MONGODB_HOST = 'localhost'
        MONGODB_PORT = '27017'
        MONGODB_TIMEOUT = 1000
        MONGODB_DATABASE = 'PERSONAL'
        URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"
        conexion =  pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT, maxPoolSize=10)
      except (Exception, pymongo.DatabaseError) as error:
        print(error)
      finally:
        return(conexion)


###Para distintas base de datos    

def read_from_db():
  cursor.execute('SELECT * FROM alumnos')
  data = cursor.fetchall()
  #print(data)
  for row in data:
    print(row)
  
def read_top_db():
  cursor.execute('select max(id) as max from alumnos')
  data = cursor.fetchall()
  print(data)
  return(data)

def insert_db_nota(tnIDAlumno,tnIDMat,tnNota):

    dateTimeObj = datetime.now()  
    timestampStr = dateTimeObj.strftime("%Y-%m-%d")

    sqlite_insert_query = "INSERT INTO notas (idAlu, idMat, fecha, nota) VALUES ("+tnIDAlumno+","+tnIDMat+",'"+timestampStr+"',"+tnNota+")"

    count = cursor.execute(sqlite_insert_query)

    conexion.commit()


####DBF
def get_dbf_rows(in_file):
    from dbfread import DBF

    for record in DBF(in_file):
        print(record)

def insert_db_nota_dbf(tnIDAlumno,tnIDMat,tnNota):
    dateTimeObj = datetime.now()  
    timestampStr = dateTimeObj.strftime("%Y-%m-%d")


def read_from_db_mongo():
  from pymongo import MongoClient
  client = MongoClient()
  db = client.personal
  listado = db.alumnos
  Peoples = listado.find()
  for People in Peoples:
    print(People)

#DBF
loDBF=""
get_dbf_rows("alumnos.dbf")
#ingresar notas
#lnIDAlumno=input("ID Alumno: ")
#lnIDMat=input("Materia: ")
#lnNota=input("Nota: ")
#Insert
#insert_db_nota_dbf(lnIDAlumno,lnIDMat,lnNota)


#MongoDB
conexion=connect("MONGO")
print(conexion.server_info())
read_from_db_mongo()



### Conecat con SQLite
conexion=connect("SQLITE")
cursor = conexion.cursor()
read_from_db()

#ingresar notas
lnIDAlumno=input("ID Alumno: ")
lnIDMat=input("Materia: ")
lnNota=input("Nota: ")

#Insert
insert_db_nota(lnIDAlumno,lnIDMat,lnNota)

cursor.close()
conexion.close()


### Conecat con MSSQL
conexion=connect("MSSQL")
cursor = conexion.cursor()
read_from_db()

#ingresar notas
lnIDAlumno=input("ID Alumno: ")
lnIDMat=input("Materia: ")
lnNota=input("Nota: ")

#Insert
insert_db_nota(lnIDAlumno,lnIDMat,lnNota)

cursor.close()
conexion.close()

### Conecat con PostgreSQL
conexion=connect("PSQL")
cursor = conexion.cursor()
read_from_db()

#ingresar notas
lnIDAlumno=input("ID Alumno: ")
lnIDMat=input("Materia: ")
lnNota=input("Nota: ")

#Insert
insert_db_nota(lnIDAlumno,lnIDMat,lnNota)

cursor.close()
conexion.close()




