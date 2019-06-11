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
        if len(matrix)==0:
            return False
        else:
            n,m=len(matrix),len(matrix[0])
            if n*m<3:
                return target==matrix[0][0] or target==matrix[1][0] or target==matrix[0][1]
            else:
                start,end=0,n*m-1
                while start+1<end:
                    mid=start+(end-start)//2
                    x,y=mid//m,mid%m
                    if matrix[x][y] == target:
                        return True
                    elif matrix[x][y] > target:
                        end = mid
                    else:
                        start = mid
                return False
      
# 34. Find First and Last Position of Element in Sorted Array    

