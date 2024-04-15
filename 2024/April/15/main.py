import ast
from solution import Solution as Solution1, TreeNode
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = queue[front]
        front += 1
        if arr[index] is not None:
            node.left = TreeNode(arr[index])
            queue.append(node.left)
        index += 1
        if index < len(arr) and arr[index] is not None:
            node.right = TreeNode(arr[index])
            queue.append(node.right)
        index += 1
    return root

def run_solutions():
    solutions = [Solution1(), Solution2(), Solution3()]
    with open('test_cases.txt', 'r') as file:
        for index, line in enumerate(file, start=1):
            arr = ast.literal_eval(line.strip())
            tree = build_tree(arr)
            print(f"Test Case {index}: {arr}")
            for i, sol in enumerate(solutions, 1):
                print(f"Solution {i} Output: {sol.sumNumbers(tree)}")
            print("----------------------")

if __name__ == '__main__':
    run_solutions()
