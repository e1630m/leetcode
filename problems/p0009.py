class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return False if x < 0 else s == s[::-1]
