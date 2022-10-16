"""
1. Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
linije)
Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]
"""

lista =  ["Pas", "Macka", "Stol"] 
rezultat = []

def funkcija():
    
    if all(isinstance(x, str) for x in lista):
        rezultat = [x for x in lista if len(x)>4]
        print(rezultat)
    else:
        print("error -> u listi nisu svi elemnti tipa string")

funkcija()