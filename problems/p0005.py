class Solution:
    def __init__(self):
        self.start = 0
        self.length = 0

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        for i in range(length - 1):
            self.addPal(s, i, i)
            self.addPal(s, i, i + 1)
        return s[self.start:self.start + self.length]

    def addPal(self, s: str, i: int, j: int) -> None:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1
        if self.length < j - i - 1:
            self.start, self.length = i + 1, j - i - 1
