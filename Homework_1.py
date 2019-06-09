#783. Minimum Distance Between BST Nodes
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.temp = None
        self.minDiff = sys.maxsize

        def inorder_traverse(node):
            if node is None:
                return
            inorder_traverse(node.left)
            if self.temp is None:
                self.temp = node
            else:
                self.minDiff = min(node.val - self.temp.val, self.minDiff)
                self.temp = node
            inorder_traverse(node.right)

        inorder_traverse(root)
        return self.minDiff



#776. Strobogrammatic Number II
class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 0:
            return [""]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else:
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = ( n - 1 ) / 2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]



#879. Output Contest Matches
class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """
    def findContestMatch(self, n):
        p = [""] * n
        for i in range(n):
            p[i] = str(i + 1)
        while(n > 1):
            for i in range(n // 2):
                p[i] = "(" + p[i] + "," + p[n - 1 - i] + ")"
            n /= 2
        return p[0]



#698. Partition to K Equal Sum Subsets
class Solution(object):


    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
