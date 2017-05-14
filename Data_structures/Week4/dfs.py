# DFS

"""input
5 # n nodes
key of i-node, left child, right child:
4 1 2 # 0 node
2 3 4 # 1 node
5 -1 -1 # 2 node
1 -1 -1 # 3 node
3 -1 -1 # 4 node
"""

# output
# in-order: слева направо
# pre-order: сверху вниз
# post-order: снизу вверх

data = "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1\n".strip().split('\n')
n = data[0]


