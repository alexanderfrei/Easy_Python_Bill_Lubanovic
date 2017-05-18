
################################################################################################
# 1. lines and points

s = "4\n4 7\n1 3\n2 5\n5 6\n"
s = s.strip().split('\n')

# sort + greedy algo

lines = []
points = []

for l in s[1:]:
    l = [int(i) for i in l.split()]
    lines.append(tuple(l))
lines = sorted(lines, key=lambda x: x[1])

for st, fn in lines:
    if not points or points and st > points[-1]:
        points.append(fn)

len(points), ' '.join([str(p) for p in points]), lines

################################################################################################
#  2. continuous backpack

s = "3 50\n 60 20\n 100 50\n 120 30\n"
s = s.strip().split('\n')
n_items, w_max = [int(i) for i in s[0].split()]

items = []
for item in s[1:]:
    item = [int(i) for i in item.split()]
    item[0] = item[0] / item[1]
    items.append(tuple(item))
items = sorted(items, key=lambda x: x[0])

w_cur, v_sum = 0, 0
while w_cur < w_max and items:
    val, w = items.pop()
    free = w_max - w_cur
    w_used = min(w, free)
    v_sum += val * w_used
    w_cur += w_used

print("{:.3f}".format(v_sum))


################################################################################################
#  3. different parts

s = "6\n"
n = int(s.strip())


def diff_parts(n):
    if n < 3:
        return [n]
    parts = []
    cumsum = 0
    for i in range(1, n):
        if 2 * i + 1 + cumsum <= n or cumsum + i == n:
            cumsum += i
            parts.append(i)
            if cumsum == n: break

    return parts


print(len(diff_parts(n)))
print(' '.join([str(i) for i in diff_parts]))

################################################################################################
#  4. Huffman codes
# heapq

from collections import Counter, namedtuple
import heapq

class Node():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

s = "abracccada"
code = huffman_encode(s)
encoded = ''.join(code[ch] for ch in s)

print(Counter(s))
print(len(code), len(encoded))
for ch in sorted(code):
    print("{}: {}".format(ch, code[ch]))
print(encoded)


# DECODE

import re
s = "4 14\na: 0\nb: 10\nc: 110\nd: 111\n01001100100111\n".strip().split('\n')
coded = s[-1]
codes = {}
for c in s[1:-1]:
    c = re.split(': ', c)
    codes[c[1]] = c[0]


def huffman_decode(coded, codes):
    tmp = ''
    decoded = ''
    for i, c in enumerate(coded):
        tmp += c
        if tmp in codes.keys():
            decoded += codes[tmp]
            tmp, i_tmp = '', i
    return (decoded)

huffman_decode(coded, codes)


# test example

def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        codes = huffman_encode(s)
        coded = "".join(codes[ch] for ch in s)
        codes = {y: x for x, y in codes.items()}
        decoded = huffman_decode(coded, codes)
        assert decoded == s, [s, decoded, coded, sorted(codes.items(), key=lambda x: x[1])]

test()