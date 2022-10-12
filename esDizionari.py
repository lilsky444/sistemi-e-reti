#DIZIONARI : una coppia fatta da una chiave e un valore (è un contenitore)

#Elenco della classe (i primi due)
d1 = {1 : "Abello", 2 : "Armando"}

#La chiave è il nome, il valore sono i voti
d2 = {"Abello" : [8, 9, 7, 10], "Armando" : [10, 10, 10, 10]}

#Indicizzazione --> NO SLICING
#Si fa mediante le chiavi
print(d1[2])
print(d2["Abello"])