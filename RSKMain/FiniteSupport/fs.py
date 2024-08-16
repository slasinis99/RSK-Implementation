from __future__ import annotations

class FiniteSupportMatrix():
    def __init__(self, m: list[list[int]]) -> None:
        self.m = m
    
    def transcribe(self) -> TranscribedMatrix:
        o = [[],[]]
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                for _ in range(0,self.m[i][j],1):
                    o[0].append(i+1)
                    o[1].append(j+1)
        return TranscribedMatrix(o)
    
    def __tex__(self) -> str:
        s = '\\begin{bmatrix}'
        for r in self.m:
            for v in r:
                s += f'{v}&'
            s = s[0:len(s)-1]
            s += f'\\\\'
        s += '\\end{bmatrix}'
        return s

class TranscribedMatrix():
    def __init__(self, m: list[list[int]]) -> None:
        self.m = m
    
    def describe(self) -> FiniteSupportMatrix:
        o = []
        for _ in range(self.m[0][-1]):
            o.append([0]*max(self.m[1]))
        for i in range(len(self.m[0])):
            o[self.m[0][i]-1][self.m[1][i]-1] += 1
        return FiniteSupportMatrix(o)
    
    def __tex__(self) -> str:
        s = f'\\begin{{pmatrix}}'
        for r in self.m:
            for v in r:
                s += f'{v}&'
            s = s[0:len(s)-1]
            s += '\\\\'
        s += '\\end{pmatrix}'
        return s