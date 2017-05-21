# сортировка слиянием
import sys
from collections import deque

def merge(arr1, arr2):

    global inv
    arr1 = deque(arr1)
    arr2 = deque(arr2)
    n_iter = len(arr1) + len(arr2)
    arr = []

    for i in range(n_iter):
        # print(arr1, arr2, inv)
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                arr.append(arr1.popleft())
            else:
                inv += len(arr1)
                arr.append(arr2.popleft())
        elif not arr2:
            arr.append(arr1.popleft())
        elif not arr1:
            arr.append(arr2.popleft())

    return arr


def merge_sort(arr, l, r):
    if l == r:
        return [arr[l]]
    else:
        mid = (l + r) // 2
        return merge(merge_sort(arr, l, mid), merge_sort(arr, mid + 1, r))

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, = next(reader)
    *arr, = next(reader)
    merge_sort(arr, 0, len(arr) - 1)
    print(inv)

if __name__ == "__main__":
    inv = 0
    main()