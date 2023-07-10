import os
import time as tm
import numpy as np

ASIENTOSN = 78900
ASIENTOSVIP = 240000
arreglo_string = np.array([['1','2','3','4','5','6'],['7','8','9','10','11','12'],['13','14','15','16','17','18'],['19','20','21','22','23','24'],['25','26','27','28','29','30'],['31','32','33','34','35','36'],['37','38','39','40','41','42']])
normales = [['1','2','3','4','5','6'],['7','8','9','10','11','12'],['13','14','15','16','17','18'],['19','20','21','22','23','24'],['25','26','27','28','29','30']]
vip = [['31','32','33','34','35','36'],['37','38','39','40','41','42']]
lista_datos = []

def mostrar_asientos():
    print("ASIENTOS DISPONIBLES")
    print('Asientos normales (1 al 30): $78900\nAsientos VIP: $240000')
    for i in range(7):
        print(arreglo_string[i][:3],arreglo_string[i][3:])


def comprar_asiento():
    numasiento = input('INGRESE EL NUMERO DE ASIENTO QUE DESEA COMPRAR\n')
    for i in range(7):
        for j in range(6):
            if numasiento == arreglo_string[i][j]:
                arreglo_string[i][j] = 'X'
                if numasiento not in normales:
                    categoria = 'VIP'
                elif numasiento not in vip:
                    categoria = 'NORMAL'
    nombrePasajero = input('INGRESE EL NOMBRE DEL PASAJERO\n') 
    rutPasajero = input('INGRESE EL RUT DEL PASAJERO\n')
    while len(rutPasajero) > 9 or len(rutPasajero) < 8:
        print('el rut ingresado no cumple el largo minimo o maximo.')
        rutPasajero = input('INGRESE EL RUT DEL PASAJERO\n')
    telefonoPasajero = input('INGRESE EL TELEFONO DEL PASAJERO\n')
    while len(telefonoPasajero) > 9 or len(telefonoPasajero) < 9:
        print('El telefono no es valido porfavor intente denuevo (CONSIDERE PONER SOLO LOS 9 NUMEROS)')
        telefonoPasajero = input('INGRESE EL TELEFONO DEL PASAJERO\n')
    bancoPasajero = input('INGRESE EL BANCO DEL PASAJERO\n')
    if bancoPasajero == 'bancoDuoc':
        dscto = True
    else:
        dscto = False
    datosuser = [numasiento,categoria,dscto,nombrePasajero,rutPasajero,telefonoPasajero,bancoPasajero]
    lista_datos.append(datosuser)
    print(arreglo_string)
    print(lista_datos)
