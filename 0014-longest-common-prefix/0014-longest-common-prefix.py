class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp=min(strs)
        for i in range(len(lcp)):
            for word in strs:
                if word[i]!=lcp[i]:
                    return lcp[:i]
        return lcp