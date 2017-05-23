# лестница

import sys


def ladder(st):

    n = len(st)
    d = [None for i in range(n)]

    d[0] = st[0]

    if n == 1:
        return st[0]
    else:
        # можем начать со второй ступеньки
        d[1] = max(st[1], st[0] + st[1])

    for i in range(2, n):
        # прошлая ступенька vs позапрошлая
        if d[i-1] + st[i] >= d[i-2] + st[i]:
            d[i] = d[i-1] + st[i]
        else:
            d[i] = d[i-2] + st[i]

    return d[n-1]


def main():
    reader = (map(int, line.strip().split()) for line in sys.stdin)
    n, = next(reader)
    *st, = next(reader)
    print(ladder(st))


if __name__ == "__main__":
    main()



