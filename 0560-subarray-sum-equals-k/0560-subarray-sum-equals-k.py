from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        prefix = 0
        count = 0
        mp = defaultdict(int)
        mp[0] = 1

        for num in nums:
            prefix += num
            count += mp[prefix - k]
            mp[prefix] += 1

        return count