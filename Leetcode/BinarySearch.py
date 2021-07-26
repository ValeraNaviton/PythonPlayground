
#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        bottom = 0
        top = len(nums)-1
        output = 0
        while bottom <= top:
            
            
            mid = int((bottom+top)/2)
  
            if top - bottom <= 1 and target!= nums[mid] and target != nums[top] and target != nums[bottom]:
                return -1
            
            if target == nums[output]:
                return output
            
        
            if target < nums[mid]:
                top = mid-1
            elif target > nums[mid]:
                bottom = mid+1
            else:
                output = mid

        
