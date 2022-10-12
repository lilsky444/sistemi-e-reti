#CIFRARIO DI CESARE
#a -> b
#b -> c

dizionarioCesare = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'z'}
messaggio = input("Inserire una parola da tradurre: ")
messaggio_tradotto = ''

for lettera in messaggio:
    messaggio_tradotto = messaggio_tradotto + dizionarioCesare[lettera]

print(messaggio_tradotto)

#for k, v in dizionario.items(): permette di scorrere il dizionario con la chive e il valore in parallelo