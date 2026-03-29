def find_leaders(arr):
    """Return leaders in arr: element >= all elements to its right."""
    n = len(arr)
    if n == 0:
        return []

    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1]


if __name__ == "__main__":
    tests = [
        [16, 17, 4, 3, 5, 2],
        [10, 4, 2, 4, 1],
        [5, 10, 20, 40],
        [30, 10, 10, 5],
    ]

    for arr in tests:
        print(f"input={arr}, leaders={find_leaders(arr)}")