class Solution:
    def myAtoi(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return ord(s) - 48 if s and s in '0123456789' else 0
        for i in range(length):
            if s[i] not in ' +-0123456789':
                return 0
            elif s[i] != ' ':
                break
        recorded, neg = '', None
        for c in s[i:]:
            if c in '0123456789':
                recorded += c
            elif not recorded:
                if c in '+-':
                    if neg is not None:
                        return 0
                    neg = c == '-'
                    continue
                return 0
            else:
                break
        recorded = '-' * neg + recorded if neg else recorded
        return max(min(2147483647, int(recorded)), -2147483648)
