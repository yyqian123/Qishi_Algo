#LeetCode 70 Climbing Stairs
class Solution:
  
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
        result=[1,2]
        for i in range(n-2):
            result.append(result[-2]+result[-1])
        return result[-1]

      
      
#LeetCode 53 Maximum Subarray
class Solution:
  
    def maxSubArray(self, nums):
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            
        return max_sum
 

    
#LeetCode 647 Palindromic Substrings
class Solution:
  
    def countPalindromicSubstrings(self, str):
        dp = [[0 for j in range(len(str))] for i in range(len(str))]
        ans = 0
        for i in range(len(str)):
            for j in range(i + 1):
                if(str[j] == str[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                    dp[j][i] = 1
                ans += dp[j][i]
        return ans

      
      
#LeetCode 359 Predict the Winner
class Solution:

    def PredictTheWinner(self, nums):
        n = len(nums)
        if n == 0:
            return True

        f = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            f[i][i] = 0

        for l in range(1, n):
            for i in range(0, n - l):
                j = i + l
                t1 = nums[i] - f[i + 1][j]
                t2 = nums[j] - f[i][j - 1]
                if t1 > t2:
                    f[i][j] = t1
                else:
                    f[i][j] = t2

        return f[0][n - 1] >= 0
