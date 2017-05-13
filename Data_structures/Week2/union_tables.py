
data = "5 5\n1 1 1 1 1\n3 5\n2 4\n1 4\n5 4\n5 3\n".strip().split('\n')
data = "6 4\n10 0 5 0 3 3\n6 6\n6 5\n5 4\n4 3\n".strip().split('\n')

n = int(data[0].split()[0])
m = int(data[0].split()[1])
r = [int(r) for r in data[1].split()]
unions = []
for i, d in enumerate(data):
    if i > 1:
        unions.append(d.split())

################################################################################################
# union by rank + compression find + O(1) max

class SetTree:

    def __init__(self, n, r):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.r = r
        self.max = max(r)

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
            print(self.max)
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            # update r
            self.r[i_id] += self.r[j_id]
            self.r[j_id] = 0
            # get max
            self.max = max(self.max, self.r[i_id])
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
            # update r
            self.r[j_id] += self.r[i_id]
            self.r[i_id] = 0
            # get max
            self.max = max(self.max, self.r[j_id])
        print(self.max)

set_tree = SetTree(n, r)
for u in unions:
    set_tree.union(int(u[0])-1, int(u[1])-1)
