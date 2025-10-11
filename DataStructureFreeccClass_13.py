# Import the heap functions (min-heap) from Python's standard library
from heapq import heappop, heappush


# Function that returns the k closest points to the origin (0, 0)
def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    # Initialize an empty min-heap
    # Each element will be a tuple: (distance, point)
    heap: list[tuple[int, list[int]]] = []

    # ------------------------------------------------------------
    # Step 1: Calculate the squared distance of each point to (0, 0)
    # and push it into the heap.
    # ------------------------------------------------------------
    for pt in points:
        # Distance formula (without sqrt): x^2 + y^2
        # We push both the distance and the point coordinates
        heappush(heap, (pt[0] ** 2 + pt[1] ** 2, pt))

    # ------------------------------------------------------------
    # Step 2: Extract the k smallest (closest) points from the heap
    # ------------------------------------------------------------
    res = []  # list to store the result

    for _ in range(k):  # repeat k times
        _, pt = heappop(heap)  # pop the point with the smallest distance
        res.append(pt)         # add it to the result list

    # Return the list of k closest points
    return res


# ------------------------------------------------------------
# Main execution block (runs only if the file is executed directly)
# ------------------------------------------------------------
if __name__ == "__main__":
    # Read the number of points
    # Each line of input contains coordinates like "x y"
    points = [list(map(int, input().split())) for _ in range(int(input()))]

    # Read the number of closest points to find
    k = int(input())

    # Call the function and store the result
    res = k_closest_points(points, k)

    # Print the list of k closest points
    print(res)
