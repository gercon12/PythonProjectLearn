#Strings O(n**2)
chars ="freecodecamp"
result = ""
for char in chars:
    result += char
print(result)

#O(n)
print("--------------------------------")
chars ="freecodecamp"
result = []
for char in chars:
    result.append(char)
    final_string = "".join(result)
print(final_string)


#Set is just a collection of unique values.  No duplicates, no particular order
set_word=  {1,2,3,4,5,6,7,8,9,10}

#O(1): run in O of one time|
nums = [1,2,3,4,5,6,7,8,9,10]
seen = set(nums)
print(3 in seen)

#Finding a value that already exists:
#No Hash Map = O(n)
#Hash map = O(1)

# Define a function called two_sum that takes a list of integers 'arr' and an integer 'target'
# It returns a list of two indices whose values add up to the target.
def two_sum(arr: list[int], target: int) -> list[int]:
    # Create an empty dictionary to store numbers and their corresponding indices.
    num_to_index = {}

    # Iterate over the array, getting both the index 'i' and the number 'num'.
    for i, num in enumerate(arr):
        # Calculate the complement that would add up with 'num' to reach the target.
        complement = target - num

        # Check if the complement already exists in the dictionary.
        if complement in num_to_index:
            # If found, return the pair of indices: index of complement and current index.
            return [num_to_index[complement], i]

        # Otherwise, store the current number and its index in the dictionary.
        num_to_index[num] = i

    # If no solution is found, return an empty list.
    return []


# Main execution block: only runs if this script is executed directly.
if __name__ == "__main__":
    # Read a line of input, split it by spaces, convert each part to int, and store as a list.
    arr = [int(x) for x in input().split()]

    # Read another input line and convert it to an integer for the target value.
    target = int(input())

    # Call the two_sum function with the input array and target.
    res = two_sum(arr, target)

    # Print the result list as a concatenated string (no spaces).
    print("".join(map(str, res)))

