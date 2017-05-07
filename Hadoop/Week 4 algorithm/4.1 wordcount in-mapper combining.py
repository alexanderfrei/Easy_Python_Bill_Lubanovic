import sys

sys.stdin = "aut Caesar aut nihil \naut aut \nde mortuis aut bene aut nihil"
sys.stdin = sys.stdin.split('\n')

for line in sys.stdin:
    d = dict()
    sentence = line.strip().split(' ')
    for term in sentence:
        if term in d:
              d[term] += 1
        else:
            d[term] = 1
    for key, value in d.items():
        print('{0}\t{1}'.format(key, value))
