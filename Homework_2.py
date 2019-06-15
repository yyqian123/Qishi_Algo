#69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        start,end=0,x
        while start+1<end:
            mid=start+(end-start)//2
            if mid**2>x:
                end=mid
            else:
                start=mid
        if end**2<=x:
            return end
        else: 
            return start
        
# 852. Peak Index in a Mountain Array  
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if A is None or len(A)<3:
            return -1
        target=A[-1]
        start,end=0,len(A)-1
        while start+1<end:
            mid=start+(end-start)//2
            if A[mid-1]<A[mid]<A[mid+1]:
                start=mid
            elif A[mid-1]>A[mid]>A[mid+1]:
                end=mid
            else:
                return mid
#74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix)==0:
            return False
        n, m = len(matrix), len(matrix[0])
        if m==0:
            return False
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid // m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start // m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end // m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
        
      
# 34. Find First and Last Position of Element in Sorted Array    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.left_index(nums, target, True)
        right=self.left_index(nums, target, False)-1
        if left==len(nums) or nums[left]!=target:
            return [-1,-1]
        return[left,right]
    
    def left_index(self,nums: List[int], target: int, left_or_right:bool):
        start,end=0,len(nums)
        while start<end:
            mid=(start+end)//2
            if nums[mid]>target or (nums[mid]==target and left_or_right):
                end=mid
            else:
                start=mid+1
        return start
        
