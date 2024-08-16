from __future__ import annotations

class SSYT():
    def __init__(self) -> None:
        self.rows: list[list[int]] = []

    def insert(self, k: int) -> None:
        row_count = len(self.rows)
        if len(self.rows) == 0:
            self.rows.append([k])
            return
        for r in self.rows:
            if r[-1] <= k:
                r.append(k)
                return
            for i, v in enumerate(r):
                if v > k:
                    r[i], k = k, r[i]
                    break
        self.rows.append([k])
    
    def __str__(self) -> str:
        s = ''
        for r in self.rows:
            for v in r:
                s += f'{v} '
            s += f'\n'
        return s[0:len(s)-1]
    
    def __tex__(self) -> str:
        s = f'\\(\\begin{{array}}{{{'c'*len(self.rows[0])}}}'
        for r in self.rows:
            for v in r:
                s += f'{v}&'
            s = s[0:len(s)-1]
            s += '\\\\'
        s += '\\end{array}\\)'
        return s

    def match_insert(self, t: SSYT, k: int) -> None:
        for i, r in enumerate(self.rows):
            if len(r) < len(t.rows[i]):
                r.append(k)
                return
        self.rows.append([k])

def rewind_tableau(P: SSYT, Q: SSYT):
    i = j = 0
    rw = cl = 0
    for u, r in enumerate(Q.rows):
        for v, val in enumerate(r):
            if val > i:
                i = val
                rw = u
                cl = v
            elif val == i and v > cl:
                rw = u
                cl = v
    j = P.rows[rw][cl]
    for u in range(rw-1, -1, -1):
        if u < 0:
            break
        for v in range(len(P.rows[u])-1, -1, -1):
            if P.rows[u][v] < j:
                P.rows[u][v], j = j, P.rows[u][v]
                break
    P.rows[rw] = P.rows[rw][0:len(P.rows[rw])-1]
    Q.rows[rw] = Q.rows[rw][0:len(Q.rows[rw])-1]
    if len(P.rows[-1]) == 0:
        P.rows = P.rows[0:len(P.rows)-1]
    if len(Q.rows[-1]) == 0:
        Q.rows = Q.rows[0:len(Q.rows)-1]
    return (i, j)