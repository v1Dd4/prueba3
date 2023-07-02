import numpy as np

array_asientos = np.zeros((7,6))
contador = 0
for i in range(7):
    for j in range(6):
        contador += 1
        array_asientos[i][j] = contador
asientos = str(array_asientos)
print(asientos)

numas = input('ingrese el asiento que desea elegir')
for i in range(7):
    for j in range(6):
        if numas == array_asientos[i][j]:
            asientos[i][j] = "x"
print(asientos)
