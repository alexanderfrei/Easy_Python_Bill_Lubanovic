import sys

sys.stdin = "1\tA\n2\tA\n2\tB\n3\tB"
sys.stdin = sys.stdin.split('\n')

# union
union = []
old_val = ""
for line in sys.stdin:
    arr = line.strip().split('\t')
    val = arr[0]
    S = arr[1]
    if (S == "A" or S == "B") and old_val != val:
        union.append(val)
    old_val = val
for el in union:
     print(el)

# intersection
inter = []
old_S = ""
old_val = ""
for line in sys.stdin:
    arr = line.strip().split('\t')
    val = arr[0]
    S = arr[1]
    if S != old_S and val == old_val:
        inter.append(val)
    old_S = S
    old_val = val
for el in inter:
     print(el)
