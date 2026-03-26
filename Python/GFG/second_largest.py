'''
arr[] = [12, 35, 1, 10, 34, 1]             -->34
arr[] = [10, 5, 10]                        -->5
arr[] = [10, 10, 10]                       -->-1
'''

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    max_val = secmax = float('-inf')
    
    for num in arr:
        if num > max_val:
            secmax = max_val
            max_val = num
        elif num > secmax and num != max_val:
            secmax = num
    
    if secmax == float('-inf'):
        return -1
    return secmax

# Even better approach: using sorted unique elements
def second_largest_better(arr):
    unique_sorted = sorted(set(arr))
    if len(unique_sorted) < 2:
        return -1
    return unique_sorted[-2]

# heapq.nlargest(n, iterable) returns n elements Larger-smaller order:O(n log k) time, good for large arrays.
import heapq
def second_largest_heap(arr):
    if len(arr) < 2:
        return -1
    top2 = heapq.nlargest(2, set(arr))  # Use set to handle duplicates
    if len(top2) < 2:
        return -1
    return top2[1]

# Test the heap approach
print(second_largest_heap([12, 35, 1, 10, 34, 1]))  # 34
print(second_largest_heap([10, 5, 10]))  # 5
print(second_largest_heap([10, 10, 10]))  # -1
