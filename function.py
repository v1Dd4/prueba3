import os
import time as tm
import numpy as np

array_asientos = np.zeros((7,6))


lista_datos = []

def comprar_asiento():
    numasiento = input('INGRESE EL NUMERO DE ASIENTO QUE DESEA COMPRAR')
    nombrePasajero = input('INGRESE EL NOMBRE DEL PASAJERO\n') 
    rutPasajero = input('INGRESE EL RUT DEL PASAJERO\n') 
    telefonoPasajero = input('INGRESE EL TELEFONO DEL PASAJERO\n+56')
    bancoPasajero = input('INGRESE EL BANCO DEL PASAJERO\n')
    datosuser = [numasiento]