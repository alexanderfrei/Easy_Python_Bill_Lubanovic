# рюкзак без повторений и с одинаковой стоимостью предметов

import sys


def knapsack_repeats(W, w, c, n):

    d = [0] * (W+1)
    for w_ind in range(W+1):
        for i in range(n):
            if w[i] <= w_ind:
                d[w_ind] = max(d[w_ind], d[w_ind - w[i]] + c[i])

    return d[W]


def knapsack_no_repeats(W, w, c, n):
    d = [[0 for i in range(n)] for w_ in range(W)]
    return d

def main():
    reader = (map(int, line.strip().split()) for line in sys.stdin)
    W, n, = next(reader)
    *w, = next(reader)
    c = [1] * len(w)
    print(knapsack_no_repeats(W, w, c, n))


if __name__ == "__main__":
    main()

