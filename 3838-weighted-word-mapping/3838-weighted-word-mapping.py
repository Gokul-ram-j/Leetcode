class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        res=""

        for word in words:
            sm=0
            for ch in word:
                sm+=weights[ord(ch)-97]
            
            res+=chr(ord("z")-(sm%26))
            
        
        return res