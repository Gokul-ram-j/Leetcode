class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d=defaultdict(int)

        while n:
            rem=n%10
            d[rem]+=1
            n//=10
        res=0
        for key,val in d.items():
            res+=(key*val)
        
        return res