# сортировка подсчетом
import sys

def count_sort(arr):
    a = [0] * len(arr)
    b = [0] * 11
    for i in arr:
        b[i] += 1
    for j in range(2, 11):
        b[j] += b[j-1]
    for i in range(len(arr)-1, -1, -1):
        tmp = arr[i]
        a[b[tmp]-1] = tmp
        b[tmp] -= 1
    return a

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, = next(reader)
    *arr, = next(reader)
    print(' '.join(map(str, count_sort(arr))))

if __name__ == "__main__":
    main()