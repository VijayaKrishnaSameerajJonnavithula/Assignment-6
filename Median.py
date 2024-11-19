import random

# Deterministic Algorithm: Median of Medians
def median_of_medians(arr, k):
    # Base case: if the array is small, sort it and return the k-th element
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Step 1: Divide the array into sublists of at most 5 elements
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of each sublist
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # Step 3: Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)
    
    # Step 4: Partition the array based on the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    
    # Find the rank of the pivot
    pivot_rank = len(low)
    
    # Step 5: Recur based on the pivot's rank and k
    if k < pivot_rank:
        return median_of_medians(low, k)
    elif k > pivot_rank:
        return median_of_medians(high, k - pivot_rank - 1)
    else:
        return pivot

# Randomized Algorithm: Randomized Quickselect
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quickselect(arr, low, high, k):
    if low == high:  # Only one element in the array
        return arr[low]
    
    pivot_index = randomized_partition(arr, low, high)
    
    if pivot_index == k:
        return arr[pivot_index]
    elif k < pivot_index:
        return randomized_quickselect(arr, low, pivot_index - 1, k)
    else:
        return randomized_quickselect(arr, pivot_index + 1, high, k)

# Function to call randomized_quickselect conveniently
def find_kth_smallest(arr, k):
    return randomized_quickselect(arr, 0, len(arr) - 1, k)

# Main function to test both algorithms
if __name__ == "__main__":
    # Test array and k value
    test_array = [3, 2, 9, 1, 5, 7, 8, 6, 4]
    k = 4  # Find the 4th smallest element (0-based index, so it's the 5th smallest in 1-based)

    # Deterministic Algorithm Output
    deterministic_result = median_of_medians(test_array.copy(), k)
    print(f"Deterministic Algorithm: {k + 1}th smallest element is {deterministic_result}")

    # Randomized Algorithm Output
    randomized_result = find_kth_smallest(test_array.copy(), k)
    print(f"Randomized Algorithm: {k + 1}th smallest element is {randomized_result}")
