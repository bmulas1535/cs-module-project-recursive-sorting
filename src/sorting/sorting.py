# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """Merged 2 given arrays. Assumes the arrays are sorted.

        Args:
            arrA(list), arrB(list): Sorted arrays

        Yields:
            merged_arr(list): Sorted array with the values from both input arrays
    """
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Create some index holders
    i, j, k = 0, 0, 0

    # Define the rules for when indexes are less than 
    # Current array lengths
    # while i < length arrA and j < length arrB:
    while i < len(arrA) and j < len(arrB):
        # if arrA[i] less than arrB[j]:
        if arrA[i] < arrB[j]:
            # merged_arr[k] is arrA[i], the lesser value
            merged_arr[k] = arrA[i]
            # increment i by 1
            i = i + 1
        # else arrB[j] is less than arrA[i]:
        # Also do this if arrB[j] is equal to arrA[i]
        else:
            # merged_arr[k] is arrB[j], the lesser value
            merged_arr[k] = arrB[j]
            # increment j by 1
            j = j + 1
        
        # increment k by 1
        k = k + 1

    # while only arrA has values left (i < length arrA):
    while i < len(arrA):
        # merged_arr[k] = arrA[i]
        merged_arr[k] = arrA[i]
        # increment both i and k by 1
        i = i + 1
        k = k + 1

    # while only arrB has values left (j < length arrB):
    while j < len(arrB):
        # merged_arr[k] = arrB[j]
        merged_arr[k] = arrB[j]
        # increment both j and k by 1
        j = j + 1
        k = k + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if the data has 1 or no elements:
    if len(arr) <= 1:
        # Do nothing
        return arr
    
    # Find the middle of the array with floor division
    # middle = length of arr // 2
    middle = len(arr) // 2
    # return the merge of merge_sort(left) and merge_sort(right) recursively
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

