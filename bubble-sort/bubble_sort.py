# Pseudo code for Bubble Sort in Python
#
# Bubble Sort repeatedly steps through the list, compares adjacent
# elements, and swaps them if they are in the wrong order. The pass
# through the list is repeated until the list is sorted.
#
# Time complexity:
#   Best case:    O(n)      -- already sorted (with optimization)
#   Average case: O(n^2)
#   Worst case:   O(n^2)
# Space complexity: O(1) -- in-place sort


# FUNCTION bubble_sort(arr):
#     n = LENGTH(arr)
#
#     FOR i FROM 0 TO n - 1:
#         swapped = FALSE
#
#         # Last i elements are already in their correct position
#         FOR j FROM 0 TO n - i - 2:
#             IF arr[j] > arr[j + 1]:
#                 SWAP arr[j] AND arr[j + 1]
#                 swapped = TRUE
#
#         # If no two elements were swapped in the inner loop,
#         # then the array is already sorted -- exit early
#         IF swapped IS FALSE:
#             BREAK
#
#     RETURN arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Early exit if the array is already sorted
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted:", sample)
    print("Sorted:  ", bubble_sort(sample))
