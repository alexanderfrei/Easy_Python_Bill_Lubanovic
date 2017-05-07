import sys
sys.stdin = "1\ta,b\n2\ta,d,e\n1\tb\n3\ta,b"
sys.stdin = sys.stdin.split('\n')
for line in sys.stdin:
    arr = line.strip().split('\t')
    F = arr[0]
    G = arr[1].split(',')    for cat in G:
        print('{0},{1}\t1'.format(F,cat))