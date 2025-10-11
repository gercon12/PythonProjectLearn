from collections import deque   # Import deque for efficient queue operations


# Define the flood fill function
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    # Get the number of rows and columns in the image
    num_rows, num_cols = len(image), len(image[0])

    # ---------------------------------------------------------
    # Nested helper function to get valid neighbor coordinates
    # ---------------------------------------------------------
    def get_neighbors(coord, color):
        row, col = coord
        # Define direction vectors for the 4-connected neighborhood
        delta_row = [-1, 0, 1, 0]  # Up, Right, Down, Left (row changes)
        delta_col = [0, 1, 0, -1]  # Up, Right, Down, Left (column changes)

        # Explore all 4 directions
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]

            # Check if neighbor coordinates are inside image boundaries
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                # Check if the neighbor pixel has the same color as the starting one
                if image[neighbor_row][neighbor_col] == color:
                    # Yield the valid neighbor coordinate (like a generator return)
                    yield neighbor_row, neighbor_col

    # ---------------------------------------------------------
    # Breadth-First Search (BFS) implementation for flood fill
    # ---------------------------------------------------------
    def bfs(root):
        # Initialize a queue with the starting pixel coordinate
        queue = deque([root])

        # Create a 2D matrix to track visited pixels
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]

        # Extract row and column from root coordinate
        r, c = root

        # Save the original color of the starting pixel
        color = image[r][c]

        # Replace the color of the starting pixel
        image[r][c] = replacement
        visited[r][c] = True

        # Process the queue until empty
        while len(queue) > 0:
            # Take the first coordinate (FIFO order)
            node = queue.popleft()

            # Explore all valid neighbors of this pixel
            for neighbor in get_neighbors(node, color):
                r, c = neighbor  # unpack neighbor coordinates

                # Skip this neighbor if already visited
                if visited[r][c]:
                    continue

                # Replace its color with the new one
                image[r][c] = replacement

                # Add this neighbor to the queue for further exploration
                queue.append(neighbor)

                # Mark it as visited
                visited[r][c] = True

    # Start BFS from the initial coordinate (r, c)
    bfs((r, c))

    # Return the modified image matrix
    return image


# ---------------------------------------------------------
# Example execution block (runs only when script is executed directly)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Example input image (2D grid)
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    # Starting pixel position
    r, c = 1, 1

    # New color to fill with
    replacement = 2

    # Apply flood fill algorithm
    result1 = flood_fill(r, c, replacement, image)
    print("----------------------------------------------------------------------")

    image1 = [
        [0, 1, 3, 4, 1],
        [3, 8, 8, 3, 3],
        [6, 7, 8, 8, 3],
        [12, 2, 8, 9, 1],
        [12, 3, 1, 3, 2]
    ]

    # Starting pixel position
    r1, c1 = 2, 2

    # New color to fill with
    replacement1 = 9


    # Apply flood fill algorithm
    result1 = flood_fill(r1, c1, replacement1, image1)

    # Print the final image matrix row by row
    for row in result1:
        print(row)
