#LeetCode 190. Reverse Bits
class Solution:

    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1
        return res

      
      
#LeetCode 201. Bitwise AND of Numbers Range
class Solution:

    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n = n & (n-1)
        return n

      
      
#LeetCode 338. Counting Bits
class Solution:

    def countBits(self, num):
        # write your code here
        f = [0] * (num + 1)
        for i in range(1, num+1):
            f[i] = f[i & i-1] + 1
        return f

      
      
#LeetCode1125. Smallest Sufficient Team

