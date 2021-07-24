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

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        if not root:
            return 0

        sum = 0

        if root.val > low:
            sum = sum + self.rangeSumBST(root.left, low, high)
        if root.val < high:
            sum = sum + self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            sum = sum + root.val
        return sum


array = TreeNode(10)
array.insert(5)
array.insert(15)
array.insert(3)
array.insert(8)
array.insert(7)
array.insert(None)
array.insert(18)
array.insert(100)
print(Solution().rangeSumBST(array, 7, 15))
