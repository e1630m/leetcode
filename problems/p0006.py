class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = ['' for _ in range(numRows)]
        row, direction, length, limit = 0, 1, len(s), numRows - 1
        for i in range(length):
            arr[row] += s[i]
            row += direction
            if not 0 < row < limit:
                direction *= -1
        return ''.join(arr)
