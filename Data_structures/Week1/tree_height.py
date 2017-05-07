# recursive search in tree with dictionaries

def tree_height(ls, node):
    h = 1
    children = ls.get(node, None)
    if children:
        for n in children:
            h = max(h, 1 + tree_height(ls, n))
    return h

import sys
sys.setrecursionlimit(20000)

# data_input = sys.stdin.read().split("\n")
data_input="""5\n-1 0 4 0 3""".split('\n')
tree_raw = [int(i) for i in data_input[1].split()]
n = int(data_input[0])

# create dictionary of parents - keys, children - value
tree = {}
for child, parent in enumerate(tree_raw):
    if parent > -1:
        tree.setdefault(parent, []).append(child)

root = tree_raw.index(-1)

print(tree_height(tree, root))


