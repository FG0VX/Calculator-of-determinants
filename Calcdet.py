# calcolates the det of matrix 2x2 and 3x3
import math as m

print("Define your matrix")
QUESTION = float(input("Is your matrix 2x2 or 3x3 ? "))

if QUESTION == 2:
    Q = float(input("Are there any roots in the matrix ?    0 = yes      1 = no:     "))
    if Q == 0:
        print("we can't solve that yet :(")
    if Q == 1:
        A = float(input("X:     "))
        B = float(input("Y:     "))
        C = float(input("Z:     "))
        D = float(input("W:     "))

        pAD = (A, D)
        pCB = (C, B)
        prAD = m.prod(pAD)
        prCB = m.prod(pCB)
        det = prAD - prCB

        print(det)

if QUESTION == 3:
    Q = float(input("Are there any roots in the matrix ?  0 = yes   1 = no: "))
    if Q == 0:
        print("we can't solve that yet :(")
    if Q == 1:
        A = float(input("a:     "))
        B = float(input("b:     "))
        C = float(input("c:     "))
        D = float(input("d:     "))
        E = float(input("e:     "))
        F = float(input("f:     "))
        G = float(input("g:     "))
        H = float(input("h:     "))
        I = float(input("i:     "))

        pEI = (E, I)
        pFH = (F, H)
        prEI = m.prod(pEI)
        prFH = m.prod(pFH)
        detEFHI = prEI - prFH

        pBI = (B, I)
        pCH = (C, H)
        prBI = m.prod(pBI)
        prCH = m.prod(pCH)
        detBCHI = prBI - prCH

        pBF = (B, F)
        pCE = (C, E)
        prBF = m.prod(pBF)
        prCE = m.prod(pCE)
        detBCEF = prBF - prCE

        DET = A * (detEFHI) - D * (detBCHI) + G * (detBCEF)
        print(DET)
