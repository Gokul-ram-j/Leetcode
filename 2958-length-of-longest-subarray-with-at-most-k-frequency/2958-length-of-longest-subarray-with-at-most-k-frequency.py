class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left = 0
        mxLen = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            mxLen = max(mxLen, right - left + 1)

        return mxLen