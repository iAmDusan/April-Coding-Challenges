class TreeNode:
    """ Definition of a binary tree node. """
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """ Calculates the sum of all root-to-leaf path numbers in the binary tree. """
        def dfs(node, current_sum):
            # Base case: If the node is None, return 0
            if not node:
                return 0

            # Form the number from the root to the current node
            current_sum = current_sum * 10 + node.val

            # If it's a leaf node, return the formed number
            if not node.left and not node.right:
                return current_sum

            # Recursively sum the numbers from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start DFS from the root with initial sum of 0
        return dfs(root, 0)
