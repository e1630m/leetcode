# 1137. N-th Tribonacci Number
# https://leetcode.com/explore/item/3986
# 39 / 39 test cases passed.
# runtime: 24ms, beats 95.40% of python3 submissions.
# memory usage: 14.3mb, beats 41.36% of python3 submissions
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a, b, c = 0, 1, 1
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c

