import sys

sys.stdin = "aut\t1\t4\naut\t2\t2\nbene\t2\t1\nde\t2\t1\nmortuis\t2\t1\nnihil\t1\t1\nnihil\t2\t1\nCaesar\t1\t1"
sys.stdin = sys.stdin.split('\n')

for line in sys.stdin:
    out = line.strip().split('\t')
    print("{0}\t{1};{2};1".format(out[0],out[1],out[2]))