class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hsh={}

        for i in nums:
            hsh[i]=hsh.get(i,0)+1
        
        for i in nums:
            if hsh[i]>1: return True
        
        return False