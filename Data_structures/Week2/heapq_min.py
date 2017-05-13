
# binary heap min

data = "5\n5 4 3 2 1".split('\n')
data = "5\n1 2 3 4 5".split('\n')
data = "6\n7 6 5 4 3 2".split('\n')
# data = "6\n0 1 2 3 4 5".split('\n')

n = int(data[0])
size = n - 1
data = [int(v) for v in data[1].strip().split()]


class MinHeap:

    def __init__(self, heap, size):
        self.heap = heap
        self.size = size
        self.print = []
        self.swap_it = 0

    # support methods
    def swap(self, i, j):
        self.print.append("{} {}".format(i, j))
        self.swap_it += 1
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sft_down(self, i):
        min_index, l, r = i, 2*i+1, 2*i+2
        if l <= self.size and self.heap[l] < self.heap[i]:
            min_index = l
        if r <= self.size and self.heap[r] < self.heap[min_index]:
            min_index = r
        if min_index != i:
            self.swap(i, min_index)
            self.sft_down(min_index)

    def build_heap(self):
        for i in range(self.size//2, -1, -1):
            self.sft_down(i)

    # priority queue methods
    def get_min(self):
        return self.heap[0]

h = MinHeap(data, size)
h.build_heap()
print(h.swap_it, '\n'.join(h.print), sep='\n')

