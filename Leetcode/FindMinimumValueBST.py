


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minValue(root) -> int:
    if root is None:
        return -1

    if root.left is None:
        return root.data
    else:
        return minValue(root.left)


class Solution:

    def findMinimum(self, root: TreeNode) -> int:
        target = root.data

        if root.left:
            target = self.findMinimum(root.left)

        return target


array = TreeNode(2)
array.left = TreeNode(1)
array.left.left = TreeNode(0)
array.right = TreeNode(81)
array.right.right = TreeNode(87)
array.right.left = TreeNode(42)
array.right.left.right = TreeNode(66)
array.right.right.right = TreeNode(90)
array.right.left.left = TreeNode(45)

print(minValue(array))
