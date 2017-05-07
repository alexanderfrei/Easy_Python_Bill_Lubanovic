import sys

sys.stdin = """1	0.067	{}
1	0.200	{2,4}
2	0.067	{}
2	0.100	{}
2	0.200	{3,5}
3	0.067	{}
3	0.100	{}
3	0.200	{4}
4	0.100	{}
4	0.200	{}
4	0.200	{5}
5	0.100	{}
5	0.200	{}
5	0.200	{1,2,3}"""

sys.stdin = sys.stdin.split("\n")
old_v = "-1"
vp = 0
vo = ""
for line in sys.stdin:
    line = line.strip()
    v = line.split("\t")[0]
    p = line.split("\t")[1]
    o = line.split("\t")[2]
    if (old_v == v or old_v == "-1") and o == "{}":
        vp += float(p)
    if (old_v == v or old_v == "-1") and o != "{}":
        vo = o
    if old_v != v and old_v != "-1":
        print("{0}\t{1:.3f}\t{2}".format(old_v, vp, vo))
        if o != "{}":
            vp = 0
            vo = o
        else:
            vp = float(p)
            vo = ""
    #print(v,p,o,p,vp)
    old_v = v
print("{0}\t{1:.3f}\t{2}".format(old_v, vp, vo))