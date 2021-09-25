# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters
# 987 / 987 test cases passed
# runtime: 60ms, beats 79.49% of python3 submissions
# memory usage: 14.2mb, beats 79.34% of python3 submissions
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
