# DFS
# поиск в глубину
# in-order: слева направо
# pre-order: сверху вниз
# post-order: снизу вверх


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


data = "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1\n".strip().split('\n')
# data = "10\n0 7 2\n10 -1 -1\n20 -1 6\n30 8 9\n40 3 -1\n50 -1 -1\n60 1 -1\n70 5 4\n80 -1 -1\n90 -1 -1".strip().split('\n')
nodes = data[1:]

# init tree
tree = BinaryTree(0)

# build tree
def build_tree(node, parent=None):
    v, l, r = [int(i) for i in nodes[node.key].split()]
    node.value = v
    node.parent = parent
    if l > -1:
        node.left = TreeNode(l)
        build_tree(node.left, node.key)
    if r > -1:
        node.right = TreeNode(r)
        build_tree(node.right, node.key)

build_tree(tree.root, None)

# pre-order read
def pre_order(node):
    if not node: return
    print(node.value, end=' ')
    pre_order(node.left)
    pre_order(node.right)


# in-order read
def in_order(node):
    if not node: return
    in_order(node.left)
    print(node.value, end=' ')
    in_order(node.right)

# post-order read
def post_order(node):
    if not node: return
    post_order(node.left)
    post_order(node.right)
    print(node.value, end=' ')

in_order(tree.root)
print()
pre_order(tree.root)
print()
post_order(tree.root)

