class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [idx for p, idx in sorted([(sum(mat[i]), i) for i in range(len(mat))])][:k]
