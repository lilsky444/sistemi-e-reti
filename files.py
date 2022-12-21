#I FILE
def leggi_file(nome_file):
    """La funzione legge il file dei matematici"""

    file = open(nome_file, "r")

    #per leggere un file e salvare le righe in una lista
    lista_righe = file.readlines()

    #print(lista_righe)

    file.close()

    diz_matematici = {"id":[], "nomi":[]} #id sono numeri, nomi sono stringhe

    for riga in lista_righe[1:]:
        #per stampare riga per riga senza andare a capo 2 volte
        riga_senza_linefeed = riga[:-1]
        lista_campi = riga_senza_linefeed.split(",") #è un metodo, la virgola è il separatore
        #.split è come l'strtok su c
        id = int(lista_campi[0])
        nome = lista_campi[1]
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])
    
    return diz_matematici

def nomeId(id, diz):
    listaId = diz["id"]
    listaNomi = diz["nomi"]

    for i,n in zip(listaId, listaNomi):
        if i == id:
            return n

def main():
    diz = leggi_file("matematici.csv")
    print(diz)

    id = int(input("Inserire l'id: "))

    nome = nomeId(id, diz)
    print(nome)

if __name__ == "__main__":
    main()