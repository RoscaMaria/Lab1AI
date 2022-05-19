import copy

from cautarAleatoare import generareSolAleatoare, fctFitness


def vecini2(sol, index):
    vecini = sol
    pozSchimbare = 0
    if vecini[index] == 0:
        vecini[index] = 1
        pozSchimbare = index
    #print("vecin din fct de creat vecini", vecini)
    return vecini, pozSchimbare
def generareTotiVec(sol):
    n = len(sol)
    index = 0
    listaVecini = []
    pozSchimbare2 = 0
    for f in range(n):
        if sol[f] == 0:
            index = f
            break

    vecini, pozSchimbare = vecini2(sol,index)

    #print("vecin din for generare toti vecini:", vecini)
    #print("pozitia la care se schimba primul vecin", pozSchimbare)
    i = pozSchimbare + 1
    #print("pozitia de la care se incepe schimbarea", i)
    vecini[pozSchimbare] = 0

    for i in range(n):
        if vecini[i] == 0:
    #        print("a trecut prin if la pozitia ", i)
            vecini[i] = 1
            pozSchimbare2 = i
   #         print("vecini din if",vecini)
  #          print(pozSchimbare2)
            vec = copy.copy(vecini)
            vec2 = copy.copy(vec)
            listaVecini.append(vec2)

        vecini[pozSchimbare2] = 0
 #       print(listaVecini)
#        print("primul sir din lista vecini", listaVecini[0])
    return listaVecini

def sach(obiecte, greutateTotala, k):
    listaVecini = []
    listaValori = []
    listaVeciniValizi = []
    p = 0
    while p<k:
        sol = generareSolAleatoare(obiecte)
        valoare, greutate = fctFitness(obiecte, sol, greutateTotala)
        i = 0
        best = valoare
        valInitiala = valoare
        if greutate:
            listaVecini = generareTotiVec(sol)
            l = len(listaVecini)
            p = p+1
            for i in range(l):
                valoare, greutate = fctFitness(obiecte, listaVecini[i], greutateTotala)
                if greutate:
                    listaValori.append(valoare)
                    listaVeciniValizi.append(listaVecini[i])

            for i in listaValori:
                if listaValori[i] > best:
                    best = listaValori[i]
                    index = i
                else:
                    return best




    print("sol", sol)
    print("vecini", listaVecini)