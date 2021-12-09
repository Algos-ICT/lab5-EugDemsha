with open("Input", "r") as fi:
    lines = fi.read().split("\n")
fo = open("Output", "w")
n = int(lines[0])
lines.pop(0)


class PriorityQueue:
    def __init__(self):
        self.heap_size = 0

    def heap_minimum(self, A):
        return A[0]

    def find_parent(self, i):
        parent = i // 2
        if i % 2 == 0:
            parent -= 1
        return parent

    def heap_decrease_key(self, A, i, key):
        if key > A[i]:
            return print("Ошибка: новый ключ больше текущего")
        A[i] = key
        parent = self.find_parent(i)
        while i > 0 and A[parent] > A[i]:
            A[i], A[parent] = A[parent], A[i]
            i = parent
            parent = self.find_parent(i)

    def min_heap_insert(self, A, key):
        A.append(float("inf"))
        self.heap_decrease_key(A, self.heap_size, key)
        self.heap_size += 1

    def min_heapify(self, A, i):
        _l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        if _l < self.heap_size and A[_l] < A[smallest]:
            smallest = _l
        if r < self.heap_size and A[r] < A[smallest]:
            smallest = r

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.min_heapify(A, smallest)

    def heap_extract_min(self, A):
        if self.heap_size < 1:
            return print("Ошибка: очередь пуста")
        max = A[0]
        A[0] = A[-1]
        A.pop(-1)
        self.heap_size -= 1
        self.min_heapify(A, 0)
        return max

l = []
a = PriorityQueue()

for action in lines:
    print(l)
    print(action)

    if action[0] == 'X':
        if l:
            fo.write(str(a.heap_extract_min(l)))
            fo.write("\n")
        else:
            fo.write('*')

    if action[0] == 'A':
        a.min_heap_insert(l, int(action.split()[1]))

    if action[0] == 'D':
        x = int(action[2]) - 1
        if lines[x][0] == "A":
            if int(lines[x].split()[1]) in l:
                i = l.index(int(lines[x].split()[1]))
                a.heap_decrease_key(l, i, int(action.split()[2]))
