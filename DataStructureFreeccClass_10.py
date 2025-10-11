# Define a class to represent a node in a binary tree
class Node:
    # Constructor: initializes the node with a value and optional left/right children
    def __init__(self, val, left=None, right=None):
        self.val = val          # The value stored in the node
        self.left = left        # Reference to the left child node
        self.right = right      # Reference to the right child node


# Function to calculate the maximum depth (or height) of a binary tree
def tree_max_depth(root: Node) -> int:
    # Inner recursive function to perform Depth-First Search (DFS)
    def dfs(root):
        # Base case: if the current node is None, the depth is 0
        if not root:
            return 0
        # Recursive case:
        # Compute the depth of left and right subtrees,
        # then take the maximum and add 1 for the current node
        return max(dfs(root.left), dfs(root.right)) + 1

    # Start the DFS from the root node
    # If the tree exists, subtract 1 to match the problem’s depth definition
    # Otherwise, return 0 for an empty tree
    return dfs(root) - 1 if root else 0


# -----------------------------------------------------------
# Function to build a binary tree from a sequence of inputs
# (used to test the algorithm easily)
# -----------------------------------------------------------
def build_tree(nodes, f):
    # Get the next value from the input iterator
    val = next(nodes)

    # If the value is "x", this represents a null (empty) node
    if val == "x":
        return None

    # Recursively build the left subtree
    left = build_tree(nodes, f)

    # Recursively build the right subtree
    right = build_tree(nodes, f)

    # Return a new Node with the converted value and its left/right children
    return Node(f(val), left, right)


# -----------------------------------------------------------
# Main program entry point (executes only when run directly)
# -----------------------------------------------------------
if __name__ == "__main__":
    # Read the tree data from input as a sequence of values
    # Example input: "1 2 x x 3 x x" (preorder representation)
    root = build_tree(iter(input().split()), int)

    # Call the function to compute the maximum tree depth
    res = tree_max_depth(root)

    # Print the result
    print(res)
