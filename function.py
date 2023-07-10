import os
import time as tm
import numpy as np


lista_datos = []

def comprar_asiento():
    numasiento = input('INGRESE EL NUMERO DE ASIENTO QUE DESEA COMPRAR\n')
    nombrePasajero = input('INGRESE EL NOMBRE DEL PASAJERO\n') 
    rutPasajero = input('INGRESE EL RUT DEL PASAJERO\n') 
    telefonoPasajero = input('INGRESE EL TELEFONO DEL PASAJERO\n+56')
    bancoPasajero = input('INGRESE EL BANCO DEL PASAJERO\n')
    datosuser = [numasiento,nombrePasajero,rutPasajero,telefonoPasajero,bancoPasajero]
    lista_datos.append[datosuser]