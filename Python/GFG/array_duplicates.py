def find_duplicates(arr):
    """Return all elements that appear twice in an array with values 1..n."""
    n = len(arr)
    result = []

    if n == 0:
        return result

    freq = [0] * (n + 1)
    for val in arr:
        if 1 <= val <= n:
            freq[val] += 1

    for val in range(1, n + 1):
        if freq[val] == 2:
            result.append(val)

    return result


if __name__ == "__main__":
    examples = [
        ([2, 3, 1, 2, 3], [2, 3]),
        ([3, 1, 2], []),
        ([1, 1, 2, 2, 3, 4, 5], [1, 2]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
    ]

    for arr, expected in examples:
        arr_copy = arr.copy()
        out = find_duplicates(arr_copy)
        print(f"input={arr}, duplicates={sorted(out)}, expected={expected}")
