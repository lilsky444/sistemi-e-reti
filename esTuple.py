#tuple: simili alle liste ma immutabili

import math

punto = (1.5, 3.6) #una coordinata

print(f"La coordinata x del punto è {punto[0]}")

triangolo = [(1.5, 3.6), (-1.0, 0.0), (5.1, 4.3)]

print(f"La coordinata del punt y del secondo vertice è: {triangolo[1][1]}")

#Area triangolo non conoscendo la base e l'altezza: 1/2 * |Xa * Yb + Ya * Xc + Xb * Yc - Xc * Yb - Yc * Xa - Xb * Ya|

area = 0.5 * ((triangolo[0][0] * triangolo[1][1]) + (triangolo[0][1] * triangolo[2][0]) + (triangolo[1][0] * triangolo[2][1]) - (triangolo[2][0] * triangolo[1][1]) - (triangolo[2][1] * triangolo[0][0]) - (triangolo[1][0] * triangolo[0][1]))
abs(area)
print({area})