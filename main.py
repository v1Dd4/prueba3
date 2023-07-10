import os
import time as tm
import numpy as np
from function import comprar_asiento,mostrar_asientos

cont = 0
run =  True

array_asientos = np.zeros((7,6))
for i in range(7):
    for j in range(6):
        cont += 1
        array_asientos[i][j] = cont

while run:
    print("Bienvenido al simulador de venta de boletos")
    print('1)VER ASIENTOS DISPONIBLES')
    print('2)COMPRAR ASIENTOS')
    print('3)ANULAR VUELO')
    print('4)MODIFICAR DATOS PASAJERO')
    print('5)SALIR')
    op = int(input('ingrese la opcion que solicita'))
    if op > 0 and op < 6:
        if op == 1:
            mostrar_asientos()
        elif op == 2:
            comprar_asiento()