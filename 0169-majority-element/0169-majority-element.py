class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq={}
        majFreq=len(nums)//2+1

        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for i in nums:
            if freq.get(i) >= majFreq :
                return i
            

            
        