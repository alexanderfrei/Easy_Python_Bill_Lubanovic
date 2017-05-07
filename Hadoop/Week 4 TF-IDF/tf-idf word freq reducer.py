import sys
import regex

sys.stdin = "aut#1\t1\naut#1\t1\naut#1\t1\naut#1\t1\naut#2\t1\naut#2\t1\nbene#2\t1\nde#2\t1\nmortuis#2\t1\nnihil#1\t1\nnihil#2\t1\nCaesar#1\t1"
sys.stdin = sys.stdin.split('\n')

old_key = "-1"
old_word = "-1"
f = False
sum = 1
for line in sys.stdin:
    word = line.strip().split('\t')[0].split('#')[0]
    key = line.strip().split('\t')[0].split('#')[1]
    if f:
        if old_word == word and old_key == key:
            sum += 1
        if old_word != word or old_key != key:
            print("{0}\t{1}\t{2}".format(old_word,old_key,sum))
            sum = 1
    else:
        f = True
    #backup = [key, word, sum]
    old_word = word
    old_key = key
print("{0}\t{1}\t{2}".format(old_word,old_key,sum))