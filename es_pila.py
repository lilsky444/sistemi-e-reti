s = "{[3+(a+b)]+8}"
pila = []
diz = {'(':')', '[':']', '{':'}'}

for c, i in enumerate(s):
    if i == "{" or i == "[" or i == "(":
        pila.append(i)
    elif i == "}" or i=="]" or i == ")":
        parentesi = pila.pop()
        if diz[parentesi] != i:
            print (f'errore  {c+1}')

if(len(pila) == 0):
    print(f"Le parentesi sono state chiuse correttamente")
else:
    print(f"Le parentesi non sono state chiuse correttamente")