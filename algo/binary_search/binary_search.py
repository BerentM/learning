from typing import Union


def search(a: list, t: Union[int, str], l=0, h=None) -> int:
    h = h or len(a) - 1
    if l > h:
        return -1
    m = l + (h - l) // 2
    if a[m] == t:
        return m
    elif t < a[m]:
        return search(a, t, l, m - 1)
    else:
        return search(a, t, m + 1, h)
