class Solution:
    def reverse(self, x: int) -> int:
        ans = int('-' + str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        return ans if -2147483649 < ans < 2147483648 else 0
