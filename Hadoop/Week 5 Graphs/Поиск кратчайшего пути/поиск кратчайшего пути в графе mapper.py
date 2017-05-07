import sys

sys.stdin = """1	0	{2,3,4}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	INF	{9,10}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}"""

sys.stdin = sys.stdin.split("\n")

for line in sys.stdin:
    line = line.strip()
    v = line.split("\t")[0]
    r = line.split("\t")[1]
    o = line.split("\t")[2]
    if o != "{}":
        arr = o.replace("{","").replace("}","").split(",")
    else:
        arr = []
    print("{0}\t{1}\t{2}".format(v,r,o))
    if len(arr) > 0:
        for el in arr:
            if r == "INF":
                print("{0}\t{1}\t{2}".format(el,"INF","{}"))
            else:
                print("{0}\t{1}\t{2}".format(el, int(r) + 1, "{}"))