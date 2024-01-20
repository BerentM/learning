from typing import Union


def search(arr: list, t: Union[int, str], low=0, high=None) -> int:
    high = high or len(arr) - 1

    if low > high:
        return -1
    mid = low + (high - low) // 2

    if arr[mid] == t:
        return mid
    elif t > arr[mid]:
        return search(arr, t, mid + 1, high)
    else:
        return search(arr, t, low, mid - 1)
