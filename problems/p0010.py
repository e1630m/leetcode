class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s) + 1, len(p) + 1
        m = [[False for _ in range(lp)] for _ in range(ls)]
        m[0][0] = True
        for i in range(2, lp):
            if p[i - 1] == '*':
                m[0][i] = m[0][i - 2]
        for i in range(1, ls):
            for j in range(1, lp):
                tmp = ('.', s[i - 1])
                if p[j - 1] in tmp:
                    m[i][j] = m[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] in tmp:
                        m[i][j] = m[i][j - 1] or m[i][j - 2] or m[i - 1][j]
                    else:
                        m[i][j] = m[i][j - 2]
        return m[-1][-1]
