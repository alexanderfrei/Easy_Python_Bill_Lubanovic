# рюкзак с повторениями и без

import sys


def knapsack_repeats(W, w, c, n):

    d = [0] * (W+1)
    for w_ind in range(W+1):
        for i in range(n):
            if w[i] <= w_ind:
                d[w_ind] = max(d[w_ind], d[w_ind - w[i]] + c[i])

    return d[W]


def knapsack_no_repeats(W, w, c, n):

    # make dummy W+1 x n+1 matrix
    d = [[None for i in range(n+1)] for w_ in range(W+1)]

    # fill first row and col with zeros
    for w_ in range(W+1): d[w_][0] = 0
    for i in range(n+1): d[0][i] = 0

    # fill matrix
    # w & c: index - 1 !!
    for i in range(1, n+1):
        for w_ in range(1, W+1):
            d[w_][i] = d[w_][i-1]
            if w[i-1] <= w_:
                d[w_][i] = max(d[w_][i], d[w_-w[i-1]][i-1] + c[i-1])
    return d[W][n]


def main():
    reader = (map(int, line.strip().split()) for line in sys.stdin)
    W, n, = next(reader)
    *w, = next(reader)
    c = w.copy()
    print(knapsack_no_repeats(W, w, c, n))


if __name__ == "__main__":
    main()

