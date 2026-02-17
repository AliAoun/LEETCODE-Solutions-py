# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
        
        dfs(root)
        return root
    
    # Time Complexity: O(n) where n is the number of nodes in the binary tree.
    # Space Complexity: O(h) where h is the height of the binary tree, due to the recursive call stack. In the worst case, it can be O(n) if the tree is skewed, and in the best case, it can be O(log n) if the tree is balanced.