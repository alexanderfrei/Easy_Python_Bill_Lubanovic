import sys

sys.stdin = "1,a\n2,a\n3,a\n1,b\n3,b\n2,d\n2,e"
sys.stdin = sys.stdin.split('\n')

for line in sys.stdin:
    G = line.strip().split(',')[1]
    print('{0}\t1'.format(G))