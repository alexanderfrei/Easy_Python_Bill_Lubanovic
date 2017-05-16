# Проверить, является ли данное двоичное дерево деревом поиска

class BinaryTree:
    def __init__(self, key):
        self.root = TreeNode(key)

class TreeNode:
    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

import sys

data = "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1\n".strip().split('\n')
# data = "10\n0 7 2\n10 -1 -1\n20 -1 6\n30 8 9\n40 3 -1\n50 -1 -1\n60 1 -1\n70 5 4\n80 -1 -1\n90 -1 -1".strip().split('\n')
data = "0\n".strip().split('\n')
# data = "3\n2 1 2\n1 -1 -1\n3 -1 -1\n".strip().split('\n')
# data = "3\n1 1 2\n2 -1 -1\n3 -1 -1\n".strip().split('\n')
# data = "5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1\n".strip().split('\n')
# data = "4\n4 1 -1\n2 2 3\n1 -1 -1\n5 -1 -1\n".strip().split('\n')

check = True
n = int(data[0])

if n:

    sys.setrecursionlimit(n + 1000)

    # init tree
    nodes = data[1:]
    tree = BinaryTree(0)

    # build tree
    def build_tree(node, parent=None):
        v, l, r = [int(i) for i in nodes[node.key].split()]
        node.value = v
        node.parent = parent
        if l != -1:
            node.left = TreeNode(l)
            build_tree(node.left, node.key)
        if r != -1:
            node.right = TreeNode(r)
            build_tree(node.right, node.key)

    build_tree(tree.root)

    current, old = None, None

    def in_order(node):
        global check, old, current
        if not node or not check: return
        in_order(node.left)
        if not old:
            old = node.value
        else:
            current = node.value
            if current <= old:
                check = False
                return
            old = current
        in_order(node.right)

    in_order(tree.root)

print('CORRECT') if check else print('INCORRECT')

