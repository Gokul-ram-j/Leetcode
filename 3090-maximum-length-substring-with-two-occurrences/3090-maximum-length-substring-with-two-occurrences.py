from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        mxLen = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            mxLen = max(mxLen, right - left + 1)

        return mxLen