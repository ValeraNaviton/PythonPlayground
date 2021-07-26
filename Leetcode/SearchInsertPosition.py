
#https://leetcode.com/problems/search-insert-position/submissions/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        bottom = 0
        top = len(nums)-1
        
        while bottom <= top:
            mid = int(top+bottom/2)
            
            if nums[mid] > target:
                top = mid - 1
            elif nums[mid] < target:
                bottom = mid + 1
            else:
                return mid
        
        return bottom
