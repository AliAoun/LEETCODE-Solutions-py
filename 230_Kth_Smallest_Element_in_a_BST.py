# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left 
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

        # time complexity = O(N) where N is the number of nodes in the BST.
        # space complexity = O(H) where H is the height of the BST, which is O(log N) for balanced trees and O(N) for skewed trees.