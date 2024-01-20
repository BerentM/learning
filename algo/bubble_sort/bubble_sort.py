def sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        swp = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swp = True
        if not swp:
            break

    return arr
