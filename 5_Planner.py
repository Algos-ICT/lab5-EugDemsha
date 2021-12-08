with open("Input", "r") as fi:
    lines = fi.read().split("\n")
fo = open("Output", "w")
n, m = [int(i) for i in lines[0].split()]
tasks = [int(i) for i in lines[1].split()]


class PriorityQueue:
    def __init__(self):
        self.heap_size = 0

    def min_heapify(self, A, i):
        _l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if _l < self.heap_size and A[_l][0] < A[largest][0]:
            largest = _l
        if _l < self.heap_size and A[_l][0] == A[largest][0] and A[_l][1] < A[largest][1]:
            largest = _l
        if r < self.heap_size and A[r][0] < A[largest][0]:
            largest = r
        if r < self.heap_size and A[r][0] == A[largest][0] and A[r][1] < A[largest][1]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.min_heapify(A, largest)

    def heap_extract_min(self, A):
        if self.heap_size < 1:
            return print("Ошибка: очередь пуста")
        max = A[0]
        A[0] = A[-1]
        A.pop(-1)
        self.heap_size -= 1
        self.min_heapify(A, 0)
        print(A)
        return max

    def find_parent(self, i):
        parent = i // 2
        if i % 2 == 0:
            parent -= 1
        return parent

    def heap_increase_key(self, A, i, key):
        if key[0] < A[i][0]:
            return print("Ошибка: новый ключ меньше текущего")
        A[i] = key
        parent = self.find_parent(i)
        while (i > 0 and A[parent][0] > A[i][0]) or (i > 0 and A[parent][0] == A[i][0] and A[parent][1] > A[i][1]):
            A[i], A[parent] = A[parent], A[i]
            i = parent
            parent = self.find_parent(i)
        print(A)

    def max_heap_insert(self, A, key):
        A.append((float("-inf"),float("-inf")))
        self.heap_increase_key(A, self.heap_size, key)
        self.heap_size += 1


heap = []
a = PriorityQueue()
for flow in range(n):
    a.max_heap_insert(heap, (0, flow))


for t in tasks:
    fo.write(str(heap[0][1]))
    fo.write(" ")
    fo.write(str(heap[0][0]))
    fo.write("\n")
    temp = heap[0]
    a.heap_extract_min(heap)
    a.max_heap_insert(heap, (t + temp[0], temp[1]))

