lista = [20, 23, 4, 5, 30, 44, 2]

max = lista[0]
min = lista[0]

for elemento in lista[1:]:
    if max < elemento:
       max = elemento
    else:
        pass      
    if min > elemento:
        min = elemento
        
print({max})
print({min})