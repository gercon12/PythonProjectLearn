# Define a function 'is_palindrome' that checks if a given string 's' is a palindrome.
# A palindrome reads the same forwards and backwards, ignoring non-alphanumeric characters and case.
def is_palindrome(s: str) -> bool:
    # Initialize two pointers: 'l' at the start, 'r' at the end of the string.
    l, r = 0, len(s) - 1

    # Continue checking until the left pointer crosses the right pointer.
    while l < r:
        # Move the left pointer forward if the character is not alphanumeric.
        while l < r and not s[l].isalnum():
            l += 1
        # Move the right pointer backward if the character is not alphanumeric.
        while l < r and not s[r].isalnum():
            r -= 1
        # Compare lowercase versions of both characters.
        # If they are not equal, the string is not a palindrome.
        if s[l].lower() != s[r].lower():
            return False
        # Move both pointers closer to the center.
        l += 1
        r -= 1

    # If all comparisons passed, the string is a palindrome.
    return True


# Main execution block: only runs if this script is executed directly.
if __name__ == "__main__":
    # Read a string from user input.
    s = input()

    # Call the is_palindrome function on the input string.
    res = is_palindrome(s)

    # Print "true" if the string is a palindrome, otherwise print "false".
    print("true" if res else "false")
