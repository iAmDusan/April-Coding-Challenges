"""
Numerical Encoding Approach (using *10):

- In this approach, each node's value is treated as a digit, and as we traverse down the tree, we form numbers by concatenating these digits based on their positions.
- Multiplying by 10 ensures that each level of the tree contributes to a different place value in the formed number. This allows us to correctly represent multi-digit numbers along the root-to-leaf paths.
- This approach is commonly used when the tree's structure carries numerical significance, such as when each root-to-leaf path represents a number.

For example:
      1
     / \
    2   3

- Root-to-leaf path 1 -> 2 represents the number 12.
- Root-to-leaf path 1 -> 3 represents the number 13.

Simple Addition Approach (not using *10):

- In this approach, each node's value is simply added to the current sum without considering its position in the formed number.
- The resulting sum represents the accumulation of values along the paths but does not encode the numbers in a structured way based on the tree's hierarchy.
- This approach might be used when the numerical significance of the tree's structure is not relevant or when the goal is simply to accumulate values along the paths without forming numbers.

For example:
      1
     / \
    2   3

- Root-to-leaf path 1 -> 2 contributes to the sum as 3.
- Root-to-leaf path 1 -> 3 contributes to the sum as 4.
"""



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
