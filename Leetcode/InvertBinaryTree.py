class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):

        if val is None:
            return

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


class Solution:

    def invertTree(self, root):
        if root:
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)

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
