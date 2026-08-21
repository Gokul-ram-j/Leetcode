class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]

        for num in nums:
            if arr1 and arr2:
                if arr1[-1]>arr2[-1]:
                    arr1.append(num)
                else:
                    arr2.append(num)
            else:
                if not arr1:
                    arr1.append(num)
                else:
                    arr2.append(num)
        
        return arr1+arr2