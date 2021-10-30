class Solution:
    def intToRoman(self, n: int) -> str:
        d, roman = 'IVXLCDM', ''
        for i in range(1, 6, 2):
            q, r = divmod(n % 10, 5)
            n //= 10
            if r < 4:
                roman += r * d[i - 1] + d[i] * q
            else:
                roman += d[i + q] + d[i - 1]
        roman += n * d[-1]
        return roman[::-1]
