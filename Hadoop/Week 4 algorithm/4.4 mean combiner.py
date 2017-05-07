import sys
sys.stdin = "www.facebook.com\t100;1\nwww.google.com\t10;1\nwww.google.com\t5;1\nwww.google.com\t15;1\nstepic.org\t60;1\nstepic.org\t100;1"
sys.stdin = sys.stdin.split('\n')
f = False
old_key = ""
sm = 0
ct = 0
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if f:
        sm += value
        ct += 1
        if old_key != key:
            print('{0}\t{1}'.format(old_key,str(sm) + ";" + str(ct)))
            sm = 0
            ct = 0
    else:
        f=True
    value = int(line.strip().split('\t')[1].split(';')[0])
    old_key = key
sm += value
ct += 1
print('{0}\t{1}'.format(key,str(sm) + ";" + str(ct)))
# if (old_b != key):
#     print('{0}\t{1}'.format(key,value))
# else:
#     print('{0}\t{1}'.format(key,sm))