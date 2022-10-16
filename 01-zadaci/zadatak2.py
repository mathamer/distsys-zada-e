"""
2. Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne
error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
liste tipa integer. Vraća novi dictionary, gdje je value element iz liste na
tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.
Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}
"""

lista = [8,7,1,]
dictionary = {1:2,2:1,3:2}
noviDictionary = {}

def funkcija():
    if isinstance(lista, list) and isinstance(dictionary, dict):
        if len(lista) == len(dictionary):
            print("isti broj")
            if all(isinstance(x, int) for x in lista):

                for k in dictionary.keys():
                    if lista[k-1] in range(5, 10):
                        noviDictionary[k] = lista[k-1]
                    else:
                        noviDictionary[k] = -1

                print(noviDictionary)
            else:
                print("error -> u listi nisu svi elemnti tipa integer")
        else:
            print("error -> nije isti broj elemenata")

    else:
        print("error -> nisu lista i dictionary")
        


funkcija()