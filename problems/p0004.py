# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays
# 2094 / 2094 test cases passed
# runtime: 80ms, beats 98.27% of python3 submissions
# memory usage: 14.5mb, beats 53.70% of python3 submissions
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums2 + nums1)
        ll = len(l)
        lh = ll // 2
        return l[lh] if ll % 2 else sum(l[lh - 1:lh + 1]) / 2
