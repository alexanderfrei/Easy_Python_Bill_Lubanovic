import sys
# sys.stdin = "cogitare\t1\nest\t1\nest\t1\nest\t1\nmilitate\t1\npotentia\t1\nScientia\t1\nVivere\t1\nVivere\t1"
# sys.stdin = sys.stdin.split('\n')
f=False
value=1
old_key=""
for line in sys.stdin:
 key = line.strip().split('\t')[0]
 if (f):
  if (old_key != key):
   print('{0}\t{1}'.format(old_key,value))
   value = 1
  else:
   value += 1
 else: f=True
 old_b = old_key #узкое место
 old_key = key
if (old_b != key):  
 print('{0}\t{1}'.format(key,1))
else:
 print('{0}\t{1}'.format(key,value))