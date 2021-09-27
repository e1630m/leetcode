class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums2 + nums1)
        ll = len(l)
        lh = ll // 2
        return l[lh] if ll % 2 else sum(l[lh - 1:lh + 1]) / 2
