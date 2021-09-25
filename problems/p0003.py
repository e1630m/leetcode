class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = longest = 0
        used = [None] * 127
        for i, c in enumerate(s):
            pos = ord(c)
            if used[pos] is not None:
                start = max(start, used[pos] + 1)
            longest = max(longest, i - start + 1)
            used[pos] = i
        return longest
