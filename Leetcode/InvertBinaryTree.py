
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def invertTree(self, root):
        if root:
            
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            
        return root
        

# [4,2,7,1,3,6,9]
array = TreeNode(4)
array.insert(2)
array.insert(7)
array.insert(1)
array.insert(3)
array.insert(6)
array.insert(9)

print(Solution().invertTree(array))
