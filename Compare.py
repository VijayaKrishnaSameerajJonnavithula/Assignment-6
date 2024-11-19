import random
import time
import matplotlib.pyplot as plt
import numpy as np

# --- Median of Medians (Deterministic) ---
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    pivot = median_of_medians(medians, len(medians) // 2)
    
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    
    pivot_rank = len(low)
    
    if k < pivot_rank:
        return median_of_medians(low, k)
    elif k > pivot_rank:
        return median_of_medians(high, k - pivot_rank - 1)
    else:
        return pivot

# --- Randomized Quickselect ---
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = randomized_partition(arr, low, high)
    
    if pivot_index == k:
        return arr[pivot_index]
    elif k < pivot_index:
        return randomized_quickselect(arr, low, pivot_index - 1, k)
    else:
        return randomized_quickselect(arr, pivot_index + 1, high, k)

def find_kth_smallest_random(arr, k):
    return randomized_quickselect(arr, 0, len(arr) - 1, k)

# --- Empirical Comparison ---
def compare_algorithms():
    input_sizes = [100, 500, 1000, 5000, 10000]
    times_mom = []
    times_rqs = []
    
    for size in input_sizes:
        # Generate a random array for each test case
        arr_random = random.sample(range(1, 100000), size)
        k = random.randint(0, size - 1)
        
        # Measure time for Median of Medians
        start_time = time.time()
        median_of_medians(arr_random.copy(), k)
        times_mom.append(time.time() - start_time)
        
        # Measure time for Randomized Quickselect
        start_time = time.time()
        find_kth_smallest_random(arr_random.copy(), k)
        times_rqs.append(time.time() - start_time)
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, times_mom, label="Median of Medians", marker='o')
    plt.plot(input_sizes, times_rqs, label="Randomized Quickselect", marker='x')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Median of Medians vs Randomized Quickselect")
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Running the comparison ---
compare_algorithms()
