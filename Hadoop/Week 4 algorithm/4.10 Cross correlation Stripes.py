import sys

sys.stdin = "a b\na b a c"
sys.stdin = sys.stdin.split('\n')

for line in sys.stdin:
    arr = line.strip().split(' ')
    for p1 in arr:
        d = dict()
        for p2 in arr:
            if p1 != p2:
                if p2 in d:
                    d[p2] += 1
                else:
                    d[p2] = 1
        f = False
        for key,val in d.items():
            val = str(val)
            if f:
                out += "," + key + ":" + val
            else:
                f = True
                out = key + ":" + val
        print('{0}\t{1}'.format(p1, out))

