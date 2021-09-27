class Solution:
    def checkArithmeticSubarrays(self, nums, l, r): #nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for s, e in zip(l, r):
            n = nums[s:e + 1]
            maxn = max(n)
            minn = min(n)
            lenn = len(n) - 1
            if maxn == minn:
                ans.append(True)
                continue
            q, rem = divmod(maxn - minn, lenn)
            if rem:
                ans.append(False)
                continue
            sn = set(n)
            while minn < maxn:
                if minn not in sn:
                    ans.append(False)
                    break
                minn += q
            if minn == maxn:
                ans.append(True)
        return ans
