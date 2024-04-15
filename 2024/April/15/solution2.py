class TreeNode:
    """ Definition of a binary tree node. """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """ Solves the problem iteratively using a stack to simulate the DFS recursion. """
        if not root:
            return 0  # If root is None, there are no numbers to sum
        
        total_sum = 0  # Initialize the sum of numbers
        stack = [(root, 0)]  # Stack for nodes and their corresponding current sums
        
        while stack:
            node, current_sum = stack.pop()  # Pop a node and the current sum formed to that node
            current_sum = current_sum * 10 + node.val  # Update the current sum by appending this node's value

            # If it is a leaf node, add the current sum to total sum
            if not node.left and not node.right:
                total_sum += current_sum

            # Push children to the stack with the updated current sum
            if node.left:
                stack.append((node.left, current_sum))
            if node.right:
                stack.append((node.right, current_sum))
        
        return total_sum
