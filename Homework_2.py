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
