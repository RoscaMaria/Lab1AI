import copy

from cautarAleatoare import generareSolAleatoare, fctFitness

#functiile vecini2 si generare toti vecini genereaza toti vecinii unei solutii
def vecini2(sol, index):
    vecini = sol
    pozSchimbare = 0
    if vecini[index] == 0:
        vecini[index] = 1
        pozSchimbare = index
    else:
        vecini[index] = 0
        pozSchimbare = index
        print("pozSchimbare", pozSchimbare)
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
    i = pozSchimbare + 1
    vecini[pozSchimbare] = 0
    print("pozSchimbare", pozSchimbare)
    for i in range(n):
        if vecini[i] == 0:
            vecini[i] = 1
            pozSchimbare2 = i
            vec = copy.copy(vecini)
            vec2 = copy.copy(vec)
            listaVecini.append(vec2)
        else:
            vecini[i] = 0
            pozSchimbare2 = i
            vec = copy.copy(vecini)
            vec2 = copy.copy(vec)
            listaVecini.append(vec2)

        vecini[pozSchimbare2] = 0
        print("lista vecini din fct de vecini", listaVecini)

    return listaVecini

# genereaza o solutie valida
def solInitValida(obiecte, greutateTotala):
    solInit = generareSolAleatoare(obiecte)
    greutate, valoare = fctFitness(obiecte, solInit, greutateTotala)
    if greutate:
        print("greutate", greutate, "valoare", valoare)
        return solInit, valoare
    else:
        solInitValida(obiecte, greutateTotala)

# steepest ascent hill climbing
def sahcR(obiecte, greutateTotala, solInit, best, k):
    print("solInit", solInit)
    print("Valoare", best)

    listaValori = []
    bestinit = best
    i = 0
    listaVecini = generareTotiVec(solInit)
    print("lista vecini genrare", listaVecini)
    listaVeciniValizi = []

    l = len(listaVecini)
    while i < k:
        for j in range(l):
            print("lista vecini", listaVecini[j])
            greutate, valoare1 = fctFitness(obiecte, listaVecini[j], greutateTotala)
            if greutate:
                listaValori.append(valoare1)
                listaVeciniValizi.append(listaVecini[j])
                i= i+1
        p = len(listaValori)
        for p in range(p):
            if listaValori[p] > best:
                best = listaValori[p]
                solInit = listaVeciniValizi[p]

        if best == bestinit:
            print("best oprit", best)
            return best
        else:
            sahcR(obiecte, greutateTotala, solInit, best, k)
    return best

#ruleaza de 10 ori functia de steepest ascent hill climbing
def run10timesSahc(k, obiecte, greutateTotala, solInit):
    i = 0
    sum = 0
    average = 0
    best = 0
    cost = 0
    indice = 0
    costuri = []
    while i<10:
        cost = sahcR(obiecte, greutateTotala, solInit, best, k)
        i=i+1
        sum = sum + cost
        costuri.append(cost)

    for p in range(10):
        if costuri[p] > best:
            best = costuri[p]
            indice = p
    print("final sum", sum)
    average = sum / 10
    print("lista costuri finale", costuri)
    print("cel mai bun cost este", costuri[indice])
    print("media este", average)
    with open('solutiiTimeSahc1.txt', 'a') as f:
        f.write(str(k))
        f.write(" ")
        f.write(str(costuri[indice]))
        f.write(" ")
        f.write(str(average))
        f.write(" ")