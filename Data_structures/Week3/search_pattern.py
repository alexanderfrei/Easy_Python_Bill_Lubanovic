
# Найти все вхождения строки Pattern в строку Text.
# search all indexes of pattern in text
# Rabin - Karp algorithm

def rabin_karp(text, pattern, d, q):
    n, m = len(text), len(pattern)
    p, t = 0, 0
    first = pow(d, m-1) % q

    for i in range(m): # hashing
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    for s in range(n-m+1):
        if p == t: # check character by character
            if pattern == text[s:s+m]:
                print(s, end=' ')
        if s < n-m:
            t = (t - first * ord(text[s])) % q # remove letter s
            t = (t*d + ord(text[s+m])) % q # add letter s+m

data = "aba\nabacaba\n".strip().split('\n')
# data = "Test\ntestTesttesT\n".strip().split('\n')
# data = "aaaaa\nbaaaaaaa\n".strip().split('\n')

pattern, s = data[0], data[1]
rabin_karp(s, pattern, 263, 1000000007)

