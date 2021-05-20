import os

from conexion import *

con = conectar()

crear_tabla(con)

def iniciar():
    os.system('cls')
    print('Seleccione una opción:')
    print('\t1. Añadir un contacto')
    print('\t2. Mostrar todos los contactos')
    print('\t3. Buscar un contacto')
    print('\t4. Modificar un contacto')
    print('\t5. Eliminar un contacto')
    print('\t6. Salir de la aplicación')
    input('')

iniciar()
