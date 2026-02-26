class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        r=0
        maxLen=0
        seen=set()
        while(r<len(s)):
            if s[r] in seen:
                while(l<r and s[r]  in seen):
                    seen.remove(s[l])
                    l+=1
            
            seen.add(s[r])
            r+=1
            maxLen=max(r-l,maxLen)
        return maxLen