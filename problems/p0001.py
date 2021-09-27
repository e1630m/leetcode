class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(n)):
            l = target - n[i]
            if l in d:
                return [d[l], i]
            d[n[i]] = i
