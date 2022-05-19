import unittest
import numpy as np

#genereaza o sol aleatoare
def generareSolAleatoare(obiecte):
    n = len(obiecte)
    sol = np.random.randint(2, size=n)
    print("prima solutie", sol)
    return sol

#evaluare si fctFitness evalueaza o solutie
def evaluare(obiecte, sol):
    greutate = 0
    valoare = 0
    l = len(obiecte)
    for i in range(l - 1):
        greutate = greutate + sol[i] * obiecte[i][1]
        valoare = valoare + sol[i] * obiecte[i][0]
    print(greutate, valoare)
    return greutate, valoare

def fctFitness(obiecte, sol, greutateTotala):
    greutate, valoare = evaluare(obiecte, sol)
    print("greutate", greutate)
    return greutate <= greutateTotala, valoare

#algoritm cautare aleatoare
def generareSolutieAleatoare(obiecte, greutateTotala, k):
    i = 0
    solutii = []
    costuri = []
    sirGreutate = []
    indice = -1
    print(i, k)
    sum = 0
    c = 0
    while i<k:
        print("a ajuns in while")
        sol = generareSolAleatoare(obiecte)
        print(sol)
        greutate, valoare = fctFitness(obiecte, sol, greutateTotala)
        print("greutate din while", greutate)
        if greutate:
            print("greutate din if", greutate)
            solutii.append(sol)
            costuri.append(valoare)
            sirGreutate.append(greutate)
            sum = sum + valoare
            c = c + 1
            i = i+1
    p = 0
    best = 0
    for p in range(k):
        if costuri[p] > best:
            best = costuri[p]
            indice = p
    average = sum/c
    print("average",average)
    with open('solutii.txt', 'a') as f:
        f.write(str(k))
        f.write(" ")
        f.write(str(costuri[indice]))
        f.write(" ")
        f.write(str(solutii[indice]))
        f.write("\n")
    print("rezultat final")
    print("solutii",solutii)
    print("costuri", costuri)
    print("sol fin", solutii[indice])
    print("cost fin", costuri[indice])
    print("greutate fin", sirGreutate[indice])
    return costuri[indice]

#ruleaza de 10 ori functia de cautare aleatoare
def run10times(k, obiecte, greutateTotala):
    i = 0
    sum = 0
    average = 0
    best = 0
    cost = 0
    indice = 0
    costuri = []
    while i<10:
        cost = generareSolutieAleatoare(obiecte, greutateTotala, k)
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
    with open('solutiiTime.txt', 'a') as f:
        f.write(str(k))
        f.write(" ")
        f.write(str(costuri[indice]))
        f.write(" ")
        f.write(str(average))
        f.write(" ")

