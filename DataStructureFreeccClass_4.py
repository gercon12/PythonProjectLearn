'''
FIXED SIZE SLIDING WINDOW
Given an array (list) nums consisted of only non-negative
integers, find the largest sum among all subarrays k in nums.
for example, if the input is [1,2,3,7,4,1], k = 3 the output would be 14
as the largest length 3 subarray sum is given by [3,7,4]
'''

def subarray_sum_fixed(nums: list[int], k: int) -> int:
    # Initialize the sum of the current window
    window_sum = 0

    # Compute the sum of the first window of size k
    for i in range(k):
        window_sum += nums[i]

    # Store the largest sum found so far
    largest = window_sum

    # Slide the window from index k to the end of the list
    for right in range(k, len(nums)):
        # Index of the element that goes out of the window
        left = right - k

        # Subtract the element that is leaving the window
        window_sum -= nums[left]

        # Add the new element that is entering the window
        window_sum += nums[right]

        # Update the maximum sum found so far
        largest = max(largest, window_sum)

    # Return the maximum sum of any subarray of size k
    return largest


if __name__ == "__main__":
    # Read a list of integers from input, separated by spaces
    nums = [int(x) for x in input().split()]

    # Read the size of the subarray (window size) from input
    k = int(input())

    # Call the function to compute the maximum subarray sum of size k
    res = subarray_sum_fixed(nums, k)

    # Print the result
    print(res)

