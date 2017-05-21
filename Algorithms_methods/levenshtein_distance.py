# расстояние Левенштейна

import sys

def leven_dist(w1, w2):
    n, m = len(w1), len(w2)
    d = [[None for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1): d[i][0] = i
    for j in range(m + 1): d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            c = not w1[i-1] == w2[j-1]
            d[i][j] = min(d[i][j-1] + 1, d[i-1][j] + 1, d[i-1][j-1] + c)

    return d[n][m]

def main():
    reader = (line.strip() for line in sys.stdin)
    *w1, = next(reader)
    *w2, = next(reader)
    print(leven_dist(w1, w2))

if __name__ == "__main__":
    main()

