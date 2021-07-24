# https://leetcode.com/problems/univalued-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        isLeftUnival = True

        isRightUnival = True

        if root is None:
            return False

        if (root.right is None) and (root.left is None):
            return True

        verification = root.val

        if root.left:
            if root.left.val != verification:
                return False
            else:
                isLeftUnival = self.isUnivalTree(root.left)

        if root.right:
            if root.right.val != verification:
                return False
            else:
                isRightUnival = self.isUnivalTree(root.right)

        return isRightUnival and isLeftUnival


array = TreeNode(2)
array.left = TreeNode(2)
array.right = TreeNode(2)
array.left.left = TreeNode(2)
array.left.right = TreeNode(2)
array.right.left = TreeNode(5)
array.right.right = TreeNode(2)

print(Solution().isUnivalTree(array))
