# наибольшая кратная подпоследовательность

import sys

def multiple_sub(arr):
    d = [0] * len(arr)
    for i in range(len(arr)):
        d[i] = 1
        for j in range(i):
            if arr[i] % arr[j] == 0 and d[i] < d[j] + 1:
                d[i] = d[j] + 1
    return max(d)

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, = next(reader)
    *arr, = next(reader)
    print(multiple_sub(arr))

if __name__ == "__main__":
    main()

