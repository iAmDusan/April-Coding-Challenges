from collections import deque

class TreeNode:
    """ Definition of a binary tree node. """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """ Uses BFS with a queue to calculate the sum of all root-to-leaf numbers. """
        if not root:
            return 0  # If the tree is empty, there's nothing to sum

        total_sum = 0  # Initialize the sum of all path numbers
        queue = deque([(root, 0)])  # Queue to hold nodes along with the path sum to that node
        
        while queue:
            node, current_sum = queue.popleft()  # Dequeue a node and the current sum to it
            current_sum = current_sum * 10 + node.val  # Update the path sum with this node's value

            # If it is a leaf node, add to the total sum
            if not node.left and not node.right:
                total_sum += current_sum

            # Enqueue children with the updated current sum
            if node.left:
                queue.append((node.left, current_sum))
            if node.right:
                queue.append((node.right, current_sum))
        
        return total_sum
