import sys
# sys.stdin = "aut Caesar aut nihil \naut aut \nde mortuis aut bene aut nihil"
# sys.stdin = sys.stdin.split('\n')
for line in sys.stdin:
 sentence = line.strip().split(' ')
 for word in sentence:
  print('{0}\t{1}'.format(word,1))