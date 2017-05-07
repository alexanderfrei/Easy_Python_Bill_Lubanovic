import sys

sys.stdin = """1	0.200	{2,4}
2	0.200	{3,5}
3	0.200	{4}
4	0.200	{5}
5	0.200	{1,2,3}"""

sys.stdin = sys.stdin.split("\n")

for line in sys.stdin:
    line = line.strip()
    v = line.split("\t")[0]
    p = line.split("\t")[1]
    o = line.split("\t")[2]
    if o != "{}":
        arr = o.replace("{","").replace("}","").split(",")
        share = float(p) / len(arr)
    print("{0}\t{1}\t{2}".format(v, p, o))
    if len(arr) > 0:
        for el in arr:
            print("{0}\t{1:.3f}\t{2}".format(el,share,"{}"))