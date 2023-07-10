import os
import time as tm
import numpy as np
from function import comprar_asiento
cont = 0
array_asientos = np.zeros((7,6))
for i in range(7):
    for j in range(6):
        cont += 1
        array_asientos[i][j] = cont
