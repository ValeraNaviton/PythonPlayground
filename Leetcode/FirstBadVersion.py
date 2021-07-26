#https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n):
        
        if n <= 0:
            return n
        
        bottom = 0
        top = n-1
        output = 0
        while bottom <= top:
            
            mid = int(bottom+(top-bottom)/2)         
        
            if isBadVersion(mid+1) == False:
                bottom = mid+1
            else:
                top = mid-1
                output = mid
        
        return output+1
        
        """
        :type n: int
        :rtype: int
        """
        
