import sys

sys.stdin = "1\tA\n2\tA\n2\tB\n3\tB"
sys.stdin = "1\tA\n2\tA\n2\tB\n3\tB"
#sys.stdin = "1\tB"
sys.stdin = sys.stdin.split('\n')

print("difference")
# difference
threshold = ""
f = False
old_S = ""
old_val = 0
for line in sys.stdin:
    setName = []
    arr = line.strip().split('\t')
    val = arr[0]
    S = arr[1]
    if f:
        if old_val != val and old_val != threshold:
            setName.append(old_S)
        if old_val == val:
            setName.append(["A","B"])
            threshold = old_val
        try:
            if setName[0] == "A":
                print(old_val)
        except IndexError:
            pass
    else:
        f = True
    backup = old_val
    old_S = S
    old_val = val
if backup != val and S == "A":
    print(val)

print("symmetric difference")
# symmetric difference sorted
threshold = ""
f = False
old_S = ""
old_val = 0
for line in sys.stdin:
    setName = []
    arr = line.strip().split('\t')
    val = arr[0]
    S = arr[1]
    if f:
        if old_val != val and old_val != threshold:
            setName.append(old_S)
        if old_val == val:
            setName = ["A","B"]
            threshold = old_val
        try:
            if len(setName) == 1:
                print(old_val)
        except IndexError:
            pass
    else:
        f = True
    backup = old_val
    old_S = S
    old_val = val
if backup != val:
    print(val)



