import queue
from collections import deque

test = """8\n2 7 3 1 5 2 6 2\n4"""

data = test.split('\n')
n = int(data[0])
m = int(data[2])
data = data[1].strip().split()
q = deque(maxlen=m)

for e in data:
    e = int(e)
    if not q:
        q.append(e)
    else:
        if e > q[-1]:
