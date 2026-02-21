class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def isPrime(n):
            if n.count('1') in [2, 3, 5, 7, 11, 13, 17, 19]:
                return True
            else:
                return False
        res=0
        for i in range(left,right+1):
            if isPrime(bin(i)): res+=1
        
        return res
