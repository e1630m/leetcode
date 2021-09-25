# 1. Two Sum
# https://leetcode.com/problems/two-sum
# 55 / 55 test cases passed
# runtime: 432ms, beats 37.54% of python3 submissions
# memory usage: 15.1mb, beats 63.29% of python3 submissions
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = []
        for i, n in enumerate(nums):
            if n in sub:
                return [nums.index(target - n), i]
            sub.append(target - n)

