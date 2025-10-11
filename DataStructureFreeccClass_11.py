# Function to count the number of islands in a binary grid (2D list)
def count_number_of_islands(grid: list[list[int]]) -> int:
    # Get the total number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # -----------------------------------------------------------
    # Helper function to find all valid neighboring coordinates
    # (up, right, down, left) within the grid boundaries
    # -----------------------------------------------------------
    def get_neighbors(coord):
        res = []                          # list to store valid neighbor coordinates
        row, col = coord                  # unpack the given coordinate (r, c)

        # Movement vectors for 4 directions:
        # up, right, down, left
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]

        # Loop through all 4 directions
        for i in range(len(delta_row)):
            r = row + delta_row[i]        # compute neighbor row
            c = col + delta_col[i]        # compute neighbor column

            # Check if neighbor is inside grid boundaries
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))        # add valid neighbor coordinate to result list

        return res                        # return all valid neighbors

    # -----------------------------------------------------------
    # Depth-First Search (DFS) recursive function
    # Marks all connected land cells as visited (turns 1 → 0)
    # -----------------------------------------------------------
    def dfs(coord):
        r, c = coord                      # unpack current coordinate
        if grid[r][c] == 0:               # base case: if it's water or already visited
            return

        grid[r][c] = 0                    # mark this land cell as visited (turn to 0)

        # Explore all valid neighbors recursively
        for neighbor in get_neighbors(coord):
            nr, nc = neighbor              # unpack neighbor coordinate
            if grid[nr][nc] == 1:          # if it's unvisited land
                dfs(neighbor)              # continue DFS recursion

    # -----------------------------------------------------------
    # Main loop: traverse the entire grid
    # Start a DFS each time we find a new island (unvisited land)
    # -----------------------------------------------------------
    count = 0                             # counter for total islands

    for r in range(num_rows):             # iterate through each row
        for c in range(num_cols):         # iterate through each column
            if grid[r][c] == 1:           # if current cell is land
                dfs((r, c))               # perform DFS to mark the island
                count += 1                # increment island count

    # Return the total number of islands found
    return count


# -----------------------------------------------------------
# Example usage: only runs when this file is executed directly
# -----------------------------------------------------------
if __name__ == "__main__":
    # Define a 2D grid where:
    # 1 represents land and 0 represents water
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    # Call the function and print the re

    print(count_number_of_islands(grid))  # Output: 3
