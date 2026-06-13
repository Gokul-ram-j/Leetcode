class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b = bin(n)[2:]
        
        cnt = 0
        for i in range(len(b) - 1):
            if b[i:i+2] == "11":
                cnt += 1
        
        return cnt == 1