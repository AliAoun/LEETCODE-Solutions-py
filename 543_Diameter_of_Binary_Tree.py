# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Returns height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res
    
    # Time Complexity: O(N) where N is the number of nodes in the tree.
    # Space Complexity: O(H) where H is the height of the tree, which is the space used by the recursion stack. Which is O(N) in the worst case (skewed tree) and O(log N) in the average case (balanced tree).