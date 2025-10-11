'''
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
Find the length of the longest substring of a given string without repeating characters.
input: abccabcabcc
output: 3
Explanation: The longest substrings are abc and cab, both of lenght 3.
input: aaaabaaa
output: 2
Explanation: ab is the longest substring, with a length of 2.
'''

from collections import defaultdict

# Import defaultdict from the collections module.
# defaultdict is a dictionary that provides a default value
# for missing keys to avoid KeyError.

def longest_substring_without_repeating_characters(s: str) -> int:
    # Define a function that receives a string 's' and
    # returns the length of the longest substring without repeating characters.

    longest = 0
    # Variable to store the length of the longest valid substring found so far.

    l = 0
    # Left pointer of the sliding window (initially at position 0).

    counter: dict[str, int] = defaultdict(int)
    # Dictionary to count the frequency of characters inside the current window.
    # Uses defaultdict(int), so missing keys will start with value 0.

    for r in range(len(s)):
        # Iterate through the string with the right pointer 'r'.
        # Each iteration expands the window to include s[r].

        counter[s[r]] += 1
        # Increment the count of the current character.

        while counter[s[r]] > 1:
            # If the current character appears more than once,
            # it means we have a duplicate in the window.

            counter[s[r]] -= 1
            # Decrease the count of the character at position l.

            l += 1
            # Move the left pointer forward to shrink the window
            # until the substring becomes valid again (no duplicates).

        longest = max(longest, r - l + 1)
        # Update the maximum length found by comparing
        # the current valid window size with the previous maximum.

    return longest
    # Return the final length of the longest substring without repeating characters.


if __name__ == '__main__':
    # Entry point of the program.
    # This code runs only if the script is executed directly.

    print(longest_substring_without_repeating_characters('abccabcabcc'))
    # Test case 1: Prints the result for the string "abccabcabcc".

    print(longest_substring_without_repeating_characters('aaaabaaa'))
    # Test case 2: Prints the result for the string "aaaabaaa".

