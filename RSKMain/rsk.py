from __future__ import annotations
from Tableau import *
from FiniteSupport import *

def rsk_forward(A: list[list[int]]) -> tuple[SSYT, SSYT]:
    A = FiniteSupportMatrix(A)
    print(A.__tex__())
    wA = A.transcribe()
    print(wA.__tex__())
    P = SSYT()
    Q = SSYT()
    for i in range(len(wA.m[0])):
        P.insert(wA.m[1][i])
        Q.match_insert(P, wA.m[0][i])
        print(f'{i+1}&{P.__tex__()}&{Q.__tex__()}\\\\\\hline')
    return (P, Q)

def rsk_backward(P: SSYT, Q: SSYT):
    print(f'P = {P.__tex__()}')
    print(f'Q = {Q.__tex__()}')
    wA = TranscribedMatrix([[],[]])
    while len(P.rows) > 0:
        i, j = rewind_tableau(P, Q)
        wA.m[0].append(i)
        wA.m[1].append(j)
    wA.m[0] = list(reversed(wA.m[0]))
    wA.m[1] = list(reversed(wA.m[1]))
    print(f'wA = {wA.__tex__()}')
    A = wA.describe()
    print(f'A = {A.__tex__()}')
    return A

A1 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
A2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
A3 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
A4 = [[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]

rsk_forward(A4)

P = SSYT()
Q = SSYT()

P.rows = [[1,2,3,4],[2,3,4],[3,4],[4]]
Q.rows = [[1,2,3,4],[2,3,4],[3,4],[4]]

# rsk_backward(P, Q)