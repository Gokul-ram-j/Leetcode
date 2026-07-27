class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0: return 0
        def digitSum(num):
            
            return s==sum([int(i) for i in str(num)])

        
        for i in range((10**n)-1,-1,-1):
             if digitSum(i):
                return i
        
        return -1