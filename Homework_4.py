#784. Letter Case Permutation
class Solution(object):
    def letterCasePermutation(self, S):
        res = []
        indices = []
        # Step 1 separate indices with characters in them.
        indices = [i for i,_ in enumerate(S) if S[i].isalpha()]
        # Step 2: Generate all subsets of the indices array of characters.
        for i in range(0, pow(2,len(indices))):
            if i==0:
                res.append(S)
            else:
                j=i;bpos=0;nsl=list(S)
                while j>0:
                    ci2c = indices[bpos] # Character index to change
                    if j&1 and S[ci2c].islower():
                        nsl[ci2c]=S[ci2c].upper()
                    elif j&1 and S[ci2c].isupper():
                        nsl[ci2c]=S[ci2c].lower()
                    bpos+=1
                    j = j >> 1
                res.append("".join(nsl))
        return res

#17. Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in range(0, len(chr[num])):
                if len(res):
                    for k in range(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(str(chr[num][j]))
            res = copy.copy(tmp)
        return res
        
#40. Combination Sum II
class Solution:    
    def combinationSum2(self, candidates, target): 
        # write your code here
        candidates.sort()        
        self.ans, tmp, use = [], [], [0] * len(candidates)        
        self.dfs(candidates, target, 0, 0, tmp, use)        
        return self.ans    
    def dfs(self, can, target, p, now, tmp, use):        
        if now == target:            
            self.ans.append(tmp[:])            
            return        
        for i in range(p, len(can)):            
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):                
                tmp.append(can[i])
                use[i] = 1                
                self.dfs(can, target, i+1, now + can[i], tmp, use)                
                tmp.pop()                
                use[i] = 0
                
#46. Permutations
class Solution:
    def permute(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

        if nums is None:
            return []
        
        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result
