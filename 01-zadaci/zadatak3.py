"""
Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
(“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) Vraća novi nested
dictionary s ključem “ukupno” i dictionary sa ključem “artikli” i listom
svih odabranih artikala te “cijena” s ukupnom cijenom računa. (Ne treba
biti One-liner)
Ispis: [{“cijena”:8,“naziv”:“Kruh”,“kolicina”:1}, {“cijena”:13,“naziv”:“Sok”,“kolicina”:2},
{“cijena”:7,“naziv”:“Upaljac”,“kolicina”:1}] -> {‘ukupno’: {‘artikli’:
[‘Kruh’, ‘Sok’, ‘Upaljac’], ‘cijena’: 57}}
"""
lista = [
    {'cijena':8,'naziv':'Kruh','kolicina':1},
     {'cijena':13,'naziv':'Sok','kolicina':2},
      {'cijena':7,'naziv':'Upaljac','kolicina':1}]

if any('cijena' and 'naziv' and 'kolicina' in keys for keys in lista):   
    print("key exists in list_of_dictionaries")  
else:  
    print("key does not exists in list_of_dictionaries")  


def funkcija():
    if isinstance(lista, list) and all(isinstance(x, dict) for x in lista):
        if len(3) == len(dictionary):
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
        print("error -> nije lista sa dictionary-ama")
        


funkcija()
