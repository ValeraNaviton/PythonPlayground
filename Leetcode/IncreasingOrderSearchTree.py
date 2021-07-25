class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def convertTreeToList(self, root: TreeNode)-> List[int]:
        
        array1 = []
        
        if root:
        
            array1.extend(self.convertTreeToList(root.left))

            array1.append(root.val)

            array1.extend(self.convertTreeToList(root.right))
        
        return array1
    
    def convertListToTree(self, array1: List[int])-> TreeNode():
        
        tree1 = TreeNode()
        tree2 = tree1
        
        for i in array1:
            tree2.right = TreeNode(i)
            tree2 = tree2.right
            
        return tree1.right

    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        array1 = self.convertTreeToList(root)
        
        return self.convertListToTree(array1)
