class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        n = 0
        for r in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            b = r in s
            n += b * d[r]
            s = s.replace(r, '')
        return n + sum(d[c] for c in s)
