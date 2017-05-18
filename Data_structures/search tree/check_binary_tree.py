# Проверить, является ли данное двоичное дерево деревом поиска

class BinaryTree:
    def __init__(self, key):
        self.root = TreeNode(key)

class TreeNode:
    def __init__(self, key, value=None, left=None, right=None, parent=None, mn=-float('Inf'), mx=float('Inf')):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.min = mn
        self.max = mx

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent


def check_tree(d):

    global check, old, max_, current
    check, current, old, max_ = True, None, None, None

    data = d.strip().split('\n')
    n = int(data[0])

    if n:

        import sys
        sys.setrecursionlimit(n + 1000)

        # init tree
        nodes = data[1:]
        tree = BinaryTree(0)

        # build tree
        def build_tree(node, parent=None):
            v, l, r = [int(i) for i in nodes[node.key].split()]
            node.value = v
            if parent:
                node.parent = parent
                if node.is_left_child():
                    node.max = parent.value
                    node.min = parent.min
                if node.is_right_child():
                    node.max = parent.max
                    node.min = parent.value
            if l != -1:
                node.left = TreeNode(l)
                build_tree(node.left, node)
            if r != -1:
                node.right = TreeNode(r)
                build_tree(node.right, node)

        build_tree(tree.root)

        def in_order(node):
            if not node: return
            in_order(node.left)
            # print(node.value, node.min, node.max)
            in_order(node.right)

        # in_order(tree.root)

        def check_node(node):
            global check
            if not check or not node: return
            if not node.is_root():
                if (node.value >= node.max or node.value < node.min) \
                        or node.is_right_child() and node.value < node.parent.value \
                        or node.is_left_child() and node.value >= node.parent.value:
                    check=False
                    return
            check_node(node.left)
            check_node(node.right)

        check_node(tree.root)

    if check:
        return 'CORRECT'
    else:
        return 'INCORRECT'

test_dict = {
    "5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1\n": "CORRECT",
    "10\n0 7 2\n10 -1 -1\n20 -1 6\n30 8 9\n40 3 -1\n50 -1 -1\n60 1 -1\n70 5 4\n80 -1 -1\n90 -1 -1\n": "INCORRECT",
    "0\n": "CORRECT",
    "3\n2 1 2\n1 -1 -1\n3 -1 -1\n": "CORRECT",
    "3\n1 1 2\n2 -1 -1\n3 -1 -1\n": "INCORRECT",
    "3\n2 1 2\n1 -1 -1\n2 -1 -1\n": "CORRECT",
    "1\n-2147483647 -1 -1": "CORRECT",
    "6\n8 1 2\n6 -1 -1\n8 3 4\n8 -1 -1\n8 5 -1\n8 -1 -1\n": "INCORRECT",
    "6\n8 -1 1\n9 -1 2\n9 3 4\n8 -1 -1\n10 -1 5\n10 -1 -1\n": "INCORRECT",
    "6\n8 1 -1\n7 2 -1\n6 3 4\n5 -1 -1\n6 -1 5\n6 -1 -1\n": "CORRECT",
    "7\n5 1 2\n3 -1 -1\n6 3 4\n5 5 -1\n6 -1 -1\n5 -1 6\n6 -1 -1\n": "INCORRECT",
    "4\n2 -1 1\n4 2 -1\n3 -1 3\n1 -1 -1\n": "INCORRECT",
    "7\n4 1 2\n2 3 4\n6 5 6\n1 -1 -1\n3 -1 -1\n5 -1 -1\n7 -1 -1": "CORRECT",
    "5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1": "CORRECT"
}

for s in test_dict.keys():
    assert check_tree(s) == test_dict[s], s

