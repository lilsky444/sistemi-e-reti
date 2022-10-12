#METODO PIU' VELOCE

n1 = int(input("Inserisci il primo numero "))
n2 = int(input("Inserisci il secondo numero "))

lista = [(n1**2) + (n2**2), (n1 + n2) ** 2, (n1**2) - (n2**2), (n1 - n2) ** 2]

print(lista)

#METODO INTERMEDIO

n1 = int(input("Inserisci il primo numero "))
n2 = int(input("Inserisci il secondo numero "))

L = []

L.append((n1**2) + (n2**2))
L.append((n1 + n2) ** 2)
L.append((n1**2) - (n2**2))
L.append((n1 - n2) ** 2)

print(L)