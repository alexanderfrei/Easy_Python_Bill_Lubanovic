
data = "2 15\n0 0 1 0 0 0 2 1 2 3 0 0 0 2 1".split('\n')
n_cores = int(data[0].split()[0])
n_tasks = int(data[0].split()[1])
tasks = [int(v) for v in data[1].strip().split()]


################################################################################################
# PriorityQueue

from queue import PriorityQueue

q = PriorityQueue(maxsize=n_cores)

# init queue
for c in range(n_cores):
    q.put((0, c))

# put + get + print with 2 priorities in tuple
for t in tasks:
    task_start, task_core = q.get()
    print('{} {}'.format(str(task_core), str(task_start)))
    q.put((task_start + t, task_core))

################################################################################################
# MinHeap


# class MinHeap:
#
#     def __init__(self, size):
#         self.size = size
#         self.heap = []
#
#     def init_heap(self):
#         for i in range(self.size+1):
#             self.heap.append([i, 0])
#
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#
#     def update(self, t):
#         self.heap[0][1] += t
#         self.sft_down(0)
#
#     def sft_down(self, i):
#         min_index, l, r = i, 2*i+1, 2*i+2
#         if l <= self.size and (self.heap[l][1] < self.heap[min_index][1] or
#                                self.heap[l][1] == self.heap[min_index][1] and
#                                            self.heap[l][0] < self.heap[min_index][0]):
#             min_index = l
#         if r <= self.size and (self.heap[r][1] < self.heap[min_index][1] or
#                                self.heap[r][1] == self.heap[min_index][1] and
#                                            self.heap[r][0] < self.heap[min_index][0]):
#             min_index = r
#         if min_index != i:
#             self.swap(i, min_index)
#             self.sft_down(min_index)
#
#     def get_min(self):
#         return '{} {}'.format(self.heap[0][0], self.heap[0][1])
#
# h = MinHeap(n_cores-1)
# h.init_heap()
# for t in tasks:
#     print(h.get_min())
#     h.update(t)

