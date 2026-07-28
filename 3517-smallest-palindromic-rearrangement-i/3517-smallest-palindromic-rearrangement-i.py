class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        d=defaultdict(int)
        for ch in s:
            d[ch]=d.get(ch,0)+1
        
        d=dict(sorted(d.items()))

        front=""
        back=""
        center=""
        for key,val in d.items():
            times=val//2
            front+=(key*times)
            back=(key*times)+back
            if val%2!=0:
                center+=key
        
        return front+center+back