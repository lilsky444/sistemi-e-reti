n = int(input("Inserisci un numero naturale n maggiore di 1: "))

primo = True

for i in range(2, n):
    if n % i==0:
        primo = False
if primo:
    print (f"è un numero primo")
else:
    print (f"non è un numero primo")