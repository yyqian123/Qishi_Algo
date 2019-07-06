# 1.Implement pow(x, n). (n is an integer.)

class Solution:
    
    def myPow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n *= (-1)

        binary = bin(n)[2:]
        ans = 1

        i = len(binary) - 1
        while i >= 0:
            if binary[i] == "1":
                ans *= x
            x = x * x
            i -= 1
        return ans
    
    
# 2.Given k strings, find the longest common prefix (LCP).

class Solution:
   
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end = end + 1
        return strs[0][:end]

      
# 3.  Merge k sorted linked lists and return it as one sorted list.

class Solution:
   
    def mergeKLists(self, lists):
        if not lists:
            return None
       
        return self.merge_range_lists(lists, 0, len(lists) - 1)
        
    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)
        
    def merge_two_lists(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
      
      
# 4. There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

class Solution:
  
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n // 2 + 1)
        else:
            smaller = self.findKth(A, 0, B, 0, n // 2)
            bigger = self.findKth(A, 0, B, 0, n // 2 + 1)
            return (smaller + bigger) / 2

    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:
            return B[index_b  + k - 1]
        if len(B) == index_b:
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])
        
        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)
