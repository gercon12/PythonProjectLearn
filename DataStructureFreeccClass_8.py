from collections import deque


# Define a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Breadth-First Search (BFS) level order traversal
def level_order_traversal(root: Node) -> list[list[int]]:
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res


# Build a binary tree from a list (e.g. [3,9,20,None,None,15,7])
def build_tree(nodes):
    if not nodes:
        return None

    root = Node(nodes[0])
    queue = deque([root])
    i = 1

    # Build the tree level by level
    while queue and i < len(nodes):
        current = queue.popleft()

        # Left child
        if i < len(nodes) and nodes[i] is not None:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1

    return root


# Main section to test
if __name__ == "__main__":
    # Example input: 3 9 20 None None 15 7
    nodes_input = input("Enter tree nodes separated by spaces (use None for nulls): ").split()
    # Convert input to integers and None
    nodes = [int(x) if x != "None" else None for x in nodes_input]

    # Build the tree
    root = build_tree(nodes)

    # Get level order traversal
    result = level_order_traversal(root)

    # Print result
    print("Level order traversal:", result)
