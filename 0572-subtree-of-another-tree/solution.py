# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isSameTree(self, r1: TreeNode | None, r2: TreeNode | None) -> bool:
        if not r1 and not r2:
            return True
        if not r1 and r2:
            return False
        if not r2 and r1:
            return False
        if r1.val != r2.val:
            return False

        return self._isSameTree(r1.left, r2.left) and self._isSameTree(r1.right, r2.right)

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root:
            return False

        if self._isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)