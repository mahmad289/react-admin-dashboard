# Pseudo code for Binary Sort (Binary Insertion Sort) in Python
#
# Binary Sort uses binary search to find the correct position
# to insert each element into the already-sorted portion of the list.
#
# FUNCTION binary_search(array, item, low, high):
#     WHILE low < high:
#         mid = (low + high) // 2
#         IF array[mid] < item:
#             low = mid + 1
#         ELSE:
#             high = mid
#     RETURN low
#
# FUNCTION binary_sort(array):
#     FOR i FROM 1 TO length(array) - 1:
#         current = array[i]
#         # Find the location to insert current using binary search
#         position = binary_search(array, current, 0, i)
#         # Shift elements to the right to make room
#         FOR j FROM i DOWN TO position + 1:
#             array[j] = array[j - 1]
#         array[position] = current
#     RETURN array
#
# EXAMPLE:
#     Input:  [5, 2, 4, 6, 1, 3]
#     Output: [1, 2, 3, 4, 5, 6]
#
# TIME COMPLEXITY:
#     - Best case:    O(n log n) comparisons, O(n) shifts
#     - Average case: O(n^2) due to shifting
#     - Worst case:   O(n^2) due to shifting
#
# SPACE COMPLEXITY: O(1) - in-place sort
