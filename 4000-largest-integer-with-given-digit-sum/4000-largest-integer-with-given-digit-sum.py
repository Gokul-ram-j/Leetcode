class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        
        def digitSum(num):
            
            return s==sum([int(i) for i in str(num)])

        max=-1
        for i in range(0,10**n):
             if digitSum(i):
                max=i
        
        if max!=-1: return max
        return -1