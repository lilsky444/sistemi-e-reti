lista = [110, 12, 45, 23, 66]

#modo preferito (pythonico)
for elemento in lista:
    print(elemento, end='-')
print()
#modo C-style
for i in range(0, len(lista)):
    print(lista[i], end='-')