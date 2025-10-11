'''
FIND THE FIRST TRUE IN A SORTED BOOLEAN ARRAY
An array boolean values is divided into two sections: The left section consists of all false, and
the right section consists of all true. Find the first True in a sorted boolean array or the right
section, i.e. the index of the first true element. If there is no true element, return -1

Input: arr =[false, false, true, true]
Output: 2

Explanation: The first true's index is 2.
'''

def find_boundary(arr: list[bool])  -> int:
    # Define a function called 'find_boundary' that takes a list of boolean values 'arr'.
    # It returns the index (integer) of the first True value in the list.
    # If no True value exists, it returns -1.

    left, right = 0, len(arr) - 1
    # Initialize two pointers:
    # 'left' starts at index 0 (the beginning of the list).
    # 'right' starts at the last index of the list.

    boundary_index = -1
    # Variable to store the index of the boundary (the first True value).
    # Initialized to -1 to represent "not found".

    while left <= right:
        # Continue searching while the left pointer does not cross the right pointer.

        mid = (left + right) // 2
        # Calculate the middle index of the current search range.

        if arr[mid]:
            # If the element at index 'mid' is True,
            # we might have found the boundary.

            boundary_index = mid
            # Save the current index as the potential boundary.

            right = mid - 1
            # Move the right pointer to the left half
            # (because there might be an earlier True).

        else:
            # If the element at 'mid' is False:

            left = mid + 1
            # Move the left pointer to the right half
            # (because the boundary must be further to the right).

    return boundary_index
    # Return the final boundary index (first True value, or -1 if not found).


if __name__ == '__main__':
    # Entry point of the program.
    # This block only runs when the script is executed directly.

    arr = [x == "true" for x in input().split()]
    # Read a line of input from the user, split it into words (tokens).
    # For each token, check if it equals the string "true".
    # Create a list of boolean values: True if the word is "true", False otherwise.

    res = find_boundary(arr)
    # Call the function 'find_boundary' with the generated boolean list
    # and store the result in variable 'res'.

    print(res)
    # Print the result: the index of the first True value, or -1 if none exist.

