'''
6. Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
Vraća se spojena lista ili dictionary.
Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]
Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}
'''

lista1 = [1,2,1,2]
lista2 = [3,2]

dictionary1 = {1:2,3:2}
dictionary2 = {5:2,4:1}

def funkcija(x,y):
    if isinstance(y, type(x)):
        # if type(x and y) == list() or type(x and y) == dict(): # moze i tako 
        if isinstance(x and y, list):
            rezultat = x + y
            return rezultat
        elif isinstance(x and y, dict):
            rezultat = x | y
            return rezultat
        else:
            print("error -> parametri nisu tipa lista ili dict")
    else:
        print("error -> parametri nisu istog tipa")

funkcija(lista1,lista2)
funkcija(dictionary1,dictionary2)

funkcija(lista1,dictionary1)