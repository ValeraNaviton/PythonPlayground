class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return True

        depth_left = self.findTreeDepth(root.left)

        if depth_left < 0:
            return False

        depth_right = self.findTreeDepth(root.right)

        if depth_right < 0:
            return False

        return abs(depth_right - depth_left) < 2


    def findTreeDepth(self, root: TreeNode) ->int:

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = 0

        right = 0

        if root.left:
            left = self.findTreeDepth(root.left)
            if left == -1:
                return -1

        if root.right:
            right = self.findTreeDepth(root.right)
            if right == -1:
                return -1

        if abs(right - left) > 1:
            return -1

        return 1+max(left, right)

array = TreeNode(3)
array.left = TreeNode(9)
array.right = TreeNode(20)
array.right.left = TreeNode(15)
array.right.right = TreeNode(7)
array.right.right.left = TreeNode(300)
array.left.left = TreeNode(1)
array.left.right = TreeNode(2)
array.left.left.left = TreeNode(12)
array.left.left.left.left = TreeNode(112)

print(Solution().isBalanced(array))
