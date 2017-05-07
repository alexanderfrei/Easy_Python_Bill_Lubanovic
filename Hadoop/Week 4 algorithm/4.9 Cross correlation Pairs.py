import sys

sys.stdin = "a b\na b a c"
sys.stdin = sys.stdin.split('\n')

for line in sys.stdin:
    arr = line.strip().split(' ')
    for p1 in arr:
        for p2 in arr:
            if p1 != p2:
                print('{0},{1}\t1'.format(p1,p2))

