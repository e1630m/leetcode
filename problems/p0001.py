class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = []
        for i, n in enumerate(nums):
            if n in sub:
                return [nums.index(target - n), i]
            sub.append(target - n)
