vocali = ['a', 'e', 'i', 'o', 'u']
carattere = 'b'

print(carattere in vocali) #in = ad appartiene 

#es vocali
s = input("Inserire una parola: ")

l = [car for car in s if car in vocali]

print(l)