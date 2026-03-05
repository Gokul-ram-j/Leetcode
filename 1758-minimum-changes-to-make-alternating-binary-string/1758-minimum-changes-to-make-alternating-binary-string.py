class Solution:
    def minOperations(self, s: str) -> int:
        op1 = 0  # starting with '0'
        op2 = 0  # starting with '1'

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    op1 += 1
                if s[i] != '1':
                    op2 += 1
            else:
                if s[i] != '1':
                    op1 += 1
                if s[i] != '0':
                    op2 += 1

        return min(op1, op2)