class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        result = TreeNode()

        if (root2 is None) and (root1 is None):
            return None

        if (root1 is None) or (root2 is None):
            if root1:
                result.val = root1.val
                if root1.left:
                    result.left = self.mergeTrees(root1.left, None)
                if root1.right:
                    result.right = self.mergeTrees(root1.right, None)

            if root2:
                result.val = root2.val
                if root2.left:
                    result.left = self.mergeTrees(None, root2.left)
                if root2.right:
                    result.right = self.mergeTrees(None, root2.right)

            return result

        elif root1 and root2:
            result.val = root1.val + root2.val
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)

        return result
        
#===================================================================================
root1 = TreeNode(11)
root1.left = TreeNode(1)
root1.right = TreeNode(20)
root1.left.left = TreeNode(-1)
root1.left.right = TreeNode(-10)

root2 = TreeNode(22)
root2.right = TreeNode(2)
root2.left = TreeNode(40)
root2.right.right = TreeNode(-2)
root2.left.right = TreeNode(-20)

res = Solution().mergeTrees(root1, root2)

print(res)
