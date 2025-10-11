# Function that checks if a given word exists in a 2D board of characters
def exist(board: list[list[str]], word: str) -> bool:
    # -------------------------------------------------------
    # Inner recursive function (Depth-First Search)
    # i, j  -> current row and column position in the board
    # word_i -> current index in the word being matched
    # -------------------------------------------------------
    def dfs(i, j, word_i):
        # If the current board cell doesn't match the target letter, stop exploring
        if board[i][j] != word[word_i]:
            return False

        # If we reached the last character and it matches, the word exists
        if word_i == len(word) - 1:
            return True

        # Temporarily store the current cell value (for backtracking later)
        char = board[i][j]
        # Mark the cell as visited (so we don't reuse it in the same path)
        board[i][j] = '*'

        # Define the 4 possible directions (up, down, left, right)
        coors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        # Explore all valid neighboring cells
        for r, c in coors:
            # Check boundaries to stay inside the board
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                # Recursively continue the search for the next letter
                if dfs(r, c, word_i + 1):
                    return True

        # Backtrack: restore the cell’s original value before returning
        board[i][j] = char
        return False

    # -------------------------------------------------------
    # Try to start DFS from every cell in the grid
    # -------------------------------------------------------
    for r in range(len(board)):           # loop over all rows
        for c in range(len(board[0])):    # loop over all columns
            # If a path starting from (r, c) can form the word, return True
            if dfs(r, c, 0):
                return True

    # If no starting position can form the word, return False
    return False


# -------------------------------------------------------
# Main program execution block
# -------------------------------------------------------
if __name__ == "__main__":
    # Read the number of rows in the board
    #board = [input().split() for _ in range(int(input()))]
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]

    # Read the word to search for
    word = input()

    # Call the function to check if the word exists
    res = exist(board, word)

    # Print the result in lowercase, as expected
    print("true" if res else "false")
