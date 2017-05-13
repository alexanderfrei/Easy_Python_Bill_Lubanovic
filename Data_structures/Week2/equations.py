
data = "4 6 0\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n".strip().split('\n')
data = "4 0 6\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n".strip().split('\n')
data = "4 6 1\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n1 2\n".strip().split('\n')

n = int(data[0].split()[0])
e = int(data[0].split()[1])
d = int(data[0].split()[2])

eq = []
n_eq = []
for i, d in enumerate(data):
    if i > 0:
        if i <= e:
            eq.append(d.split())
        else:
            n_eq.append(d.split())

################################################################################################
# union by rank + compression find


class SetTree:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def make_set(self, i):
        self.parent[i] = i

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

    def check(self, i, j):
        return self.find(i) != self.find(j)

set_tree = SetTree(n)

# fill equations tree
for i in eq:
    set_tree.union(int(i[0])-1, int(i[1])-1)

# check not equals
check = 1
for i in n_eq:
    if not set_tree.check(int(i[0]) - 1, int(i[1]) - 1):
        check = 0
        break
print(check)
