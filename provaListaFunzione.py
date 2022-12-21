l = ['ciao', print, 1, 3.24]

#Per ciclare sia l'indice che l'elemento in una lista
for indice, elemento in enumerate(l):
    print(indice, elemento)

indice = 0
for elemento in l:
    print(indice, elemento)
    indice = indice + 1