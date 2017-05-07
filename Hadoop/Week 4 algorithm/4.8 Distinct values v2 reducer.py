import sys

sys.stdin = "1\ta\n1\tb\n1\tb\n2\ta\n2\td\n2\te\n3\ta\n3\tb"
sys.stdin = sys.stdin.split('\n')

d = dict()
oF = ""
oG = ""
for line in sys.stdin:
    arr = line.strip().split('\t')
    F = arr[0]
    G = arr[1]
    if oG != G or oF != F:
        if G in d   :
            d[G] += 1
        else:
            d[G] = 1
    oF = F
    oG = G

for key,value in d.items():
    print('{0}\t{1}'.format(key,value))