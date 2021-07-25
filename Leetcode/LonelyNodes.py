from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def visitNode(self, root) -> List[int]:
        result = []
        if root.left:
            result.extend(self.visitNode(root.left))
        if root.right:
            result.extend(self.visitNode(root.right))

        if (root.left is None) ^ (root.right is None):
            if root.left:
                result.append(root.left.val)
            elif root.right:
                result.append(root.right.val)

        return result


array = TreeNode(4)
array.left = TreeNode(11)
array.right = TreeNode(100)
array.right.right = TreeNode(3)
array.right.right.right = TreeNode(17)
array.left.left = TreeNode(1)
array.left.right = TreeNode(2)

res = Solution().visitNode(array)
print(res)
