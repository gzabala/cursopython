import BasesDeDatos

#with BasesDeDatos.ConexionBD("localhost", "root", "cursopython", "personal") as base:
with BasesDeDatos.ConexionBD("db4free.net", "rootzabala", "cursopython", "personalzabala") as base:
    #base.cur.execute("SHOW TABLES")
    base.cur.execute("Select * from alumnos")
    for ele in base.cur:
        print(ele)

