import sys

sys.stdin = """1	0	{2,3,4}
10	INF	{}
10	INF	{}
2	1	{}
2	1	{5,6}
3	1	{}
3	1	{}
4	1	{}
4	1	{7,8}
5	2	{}
5	INF	{9,10}
6	2	{}
6	INF	{}
7	2	{}
7	INF	{}
8	2	{}
8	INF	{}
9	INF	{}
9	INF	{}"""

sys.stdin = """1\t0\t{2}
2\t1\t{}
2\t1\t{1}"""
sys.stdin = """4\t1\t{}
4\t2\t{}
4\t3\t{}"""


sys.stdin = sys.stdin.split("\n")
old_v = "-1"
out_1 = "-1"
out_2 = "-1"
for line in sys.stdin:
    line = line.strip()
    v = line.split("\t")[0]
    r = line.split("\t")[1]
    o = line.split("\t")[2]
    if old_v != v and old_v != "-1":
        print("{0}\t{1}\t{2}".format(old_v, out_1, out_2))
        out_1 = "-1"
        out_2 = "-1"
    if out_1 == "-1":
        out_1 = r
    else:
        if r != "INF" and r < out_1:
            out_1 = r
    if out_2 == "-1":
        out_2 = o
    else:
        if o != "{}":
            out_2 = o
    old_v = v
print("{0}\t{1}\t{2}".format(v, out_1, out_2))
