class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hsh={}
        res=[]
        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in hsh:
                return [hsh[diff],i]
            
            hsh[nums[i]]=i
        
        print(res)
        
