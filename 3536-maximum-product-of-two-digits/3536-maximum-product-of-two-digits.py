class Solution:
    def maxProduct(self, n: int) -> int:
        
        digits=sorted([int(i) for i in str(n)])

        return digits[-2]*digits[-1]