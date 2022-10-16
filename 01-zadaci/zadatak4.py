"""
4. Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
(Funkcija mora imati dvije linije)
Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]
"""

lista = [1,2,3,4,5]
lista2 = [2,2,4,4,5]
novilista = []

def funkcija():
    if len(lista) == len(lista2):
        #novilista = [x for x in lista if x in lista2] ???

        for i in range(len(lista)):
            if lista[i] == lista2[i]:
                novilista.append(lista[i])
            else:
                novilista.append(-1)

        return novilista
    else:
        print("error -> nije isti broj elemenata")
        
funkcija()

