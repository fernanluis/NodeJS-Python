from sqlite3.dbapi2 import Cursor
from conexion import *

def registrar(nombres, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contacto
            (nombres, apellidos, empresa, telefono, email, direccion) values
            (?,?,?,?,?,?
        )'''
        datos = (nombres, apellidos, empresa, telefono, email, direccion) # tupla de los datos
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'

    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
    	con = conectar()
    	cursor = con.cursor()
    	sentencia_sql = ''' SELECT * FROM contacto '''
    	cursor.execute(sentencia_sql)
    	datos = cursor.fetchall() # asignación de los resultados a la lista de datos
    	con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error')
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contacto WHERE id=? '''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def modificar(id, nombre ,apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' UPDATE contacto SET nombre=?, apellidos=?,
        empresa=?, telefono=?, email=?, direccion=?, WHERE id=? '''
        datos = (nombre, apellidos, empresa, telefono, email, direccion, id )
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return "Se actualizó correctamente."
    except sqlite3.Error as err :
        print('Ha ocurrido un error', err)

def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' DELETE FROM contacto where id=? '''
        cursor.execute(sentencia_sql, (id,))
        con.commit()
        con.close()
        return "Se eliminó correctamente"
    except sqlite3.Error as err:
        print('Ha ocurrido un error')

