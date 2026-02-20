class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        mxLn=0
        res=""
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j]==s[i:j][::-1] and mxLn<=len(s[i:j]):
                    mxLn=max(len(s[i:j]),mxLn)
                    res=s[i:j]
        return res