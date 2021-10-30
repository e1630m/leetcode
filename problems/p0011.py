class Solution:
    def maxArea(self, h: List[int]) -> int:
        w, l, r = 0, 0, len(h) - 1
        while l < r:
            if w < (t := min(h[l], h[r]) * (r - l)):
                w = t
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return w