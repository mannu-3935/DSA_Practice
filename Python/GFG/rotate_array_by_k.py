'''
Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
'''

def rotateArr(self, arr, d):
    n = len(arr)
    if n == 0:
        return arr
    d =d % n
    return arr[d:] + arr[:d]

    '''if d == 0:
        return arr
    arr[:] = arr[d:] + arr[:d]
    return arr'''

print(rotateArr(None, [1, 2, 3, 4, 5], 2))
print(rotateArr(None, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3))
print(rotateArr(None, [7, 3, 9, 1], 9))     
print(rotateArr(None, [], 3))