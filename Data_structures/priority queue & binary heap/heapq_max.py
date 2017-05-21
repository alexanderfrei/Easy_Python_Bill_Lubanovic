s = "6\nInsert 200\nInsert 10\nExtractMax\nInsert 5\nInsert 500\nExtractMax\n"
s = s.strip().split('\n')
import heapq
h = []
heapq.heapify(h)
for c in s[1:]:
    if c == 'ExtractMax' and h:
        print(heapq.heappop(h) * -1)
    if c != 'ExtractMax' :
        cv = int(c.split(' ')[1]) * -1
        heapq.heappush(h, cv)
