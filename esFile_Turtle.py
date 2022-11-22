import turtle

def leggi_file(nome_file):

    file = open(nome_file, "r")

    #per leggere un file e salvare le righe in una lista
    lista_righe = file.readlines()

    #print(lista_righe)

    file.close()

    diz = {"direzione":[], "valore":[]}

    for riga in lista_righe[0:]:
        #per stampare riga per riga senza andare a capo 2 volte
        riga_senza_linefeed = riga[:-1]
        lista_campi = riga_senza_linefeed.split(",") #è un metodo, la virgola è il separatore
        #.split è come l'strtok su c
        direzione = lista_campi[0]
        valore = lista_campi[1]
        diz["direzione"].append(direzione)
        diz["valore"].append(valore[1:])
    
    return diz

def foreward(ogg, v):
    ogg.foreward(v)

def right(ogg, v):
    ogg.right(v)

def left(ogg, v):
    ogg.left(v)

def backward(ogg, v):
    ogg.backward(v)


def main():
    finestra = turtle.Screen()

    ogg = turtle.Turtle()

    diz = leggi_file("direzion.csv")
    #print(diz)

    for k, v in zip(diz["direzione"], diz["valore"]):
        if k == "foreward":
            print(f"ciao")
            foreward(ogg, v)
        elif k == 'right':
            right(ogg, v)
        elif k == 'left':
            left(ogg, v)
        elif k == 'backward':
            backward(ogg, v)

    turtle.done()

if __name__ == "__main__":
    main()