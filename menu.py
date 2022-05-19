from cautarAleatoare import generareSolutieAleatoare, run10times
from sahcRecursiv import solInitValida, sahcR, generareTotiVec, run10timesSahc
import time


def run():
    start = time.time()
    f = open("rucsac5.txt", "r")
    s = f.readline()
    nrObiecte = int(s)
    greutateTotala = 0
    obiecte = []
    while s:
        x = s.split()
        if len(x) > 1:
            obiecte.append([int(x[1]), int(x[2])])
        else:
            if len(x) == 1:
                greutateTotala = int(x[0])
        s = f.readline()
    f.close()
    print (obiecte)
    print("greutate totala", greutateTotala)
    print("nr obiect", nrObiecte)


   # generareSolutieAleatoare(obiecte, greutateTotala, k)

    i = int(input("Alegeti 1 sau 2 pentru 1. Cautarea aleatoare, 2. Steepest ascent hill climbing:"))
    k = int(input("k:"))
    if i == 1:
        run10times(k, obiecte, greutateTotala)
        time.sleep(1)
        end = time.time()
        with open('solutiiTime.txt', 'a') as f:
            f.write(str({end - start}))
            f.write("\n")
    else:
        if i == 2:

            #sach(obiecte, greutateTotala, k)
            solInit, valoare = solInitValida(obiecte, greutateTotala)
            #sahcR(obiecte, greutateTotala, solInit, valoare, k)
            run10timesSahc(k, obiecte, greutateTotala, solInit)
            #generareTotiVec(solInit)
            time.sleep(1)
            end = time.time()
            with open('solutiiTimeSahc1.txt', 'a') as f:
                f.write(str({end - start}))
                f.write("\n")
run()