import ast
from solution import Solution as Solution1, TreeNode
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3

def build_tree(arr):
    """
    Constructs a binary tree from a level-order list representation where `None` indicates a missing node.
    This function initializes the root from the first element, then uses a queue to iterate through the list
    and build the tree by attaching left and right children as specified in the list.
    """
    if not arr:
        return None  # Return None if the input list is empty (no tree to build)

    root = TreeNode(arr[0])  # Create the root node from the first element
    queue = [root]  # A queue to keep track of nodes to attach children to
    front = 0  # Index for the current node in the queue
    index = 1  # Index in the list for the next child node

    while index < len(arr):  # Loop through the list to assign children to nodes
        node = queue[front]
        front += 1
        if arr[index] is not None:  # If there's a left child, create and attach it
            node.left = TreeNode(arr[index])
            queue.append(node.left)
        index += 1
        if index < len(arr) and arr[index] is not None:  # If there's a right child, create and attach it
            node.right = TreeNode(arr[index])
            queue.append(node.right)
        index += 1

    return root

def run_solutions():
    """
    Reads test cases from a file and applies each solution to each test case.
    Outputs the result for each solution, helping to verify the correctness and compare outputs.
    """
    solutions = [Solution1(), Solution2(), Solution3()]  # Instances of solution classes
    with open('test_cases.txt', 'r') as file:  # Open and read the test cases file
        for index, line in enumerate(file, start=1):
            arr = ast.literal_eval(line.strip())  # Parse each line into a list
            tree = build_tree(arr)  # Build the tree from the list
            print(f"Test Case {index}: {arr}")  # Print the test case information
            for i, sol in enumerate(solutions, 1):  # Loop through each solution to compute results
                print(f"Solution {i} Output: {sol.sumNumbers(tree)}")  # Display output from each solution
            print("----------------------")  # Separator for test case outputs

if __name__ == '__main__':
    run_solutions()  # Execute the function to process the test cases
