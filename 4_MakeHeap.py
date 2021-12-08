with open("Input", "r") as fi:
    lines = fi.read().split("\n")
fo = open("Output", "w")
n = int(lines[0])
massive = [int(i) for i in lines[1].split()]
heap = []


def min_heapify(A, i):
    heap_size = len(A)
    _l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if _l < heap_size and A[_l] < A[smallest]:
        smallest = _l
    if r < heap_size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        heap.append((i, smallest))
        min_heapify(A, smallest)


def build_min_heap(A):
    heap_size = len(A)
    for i in reversed(range(heap_size // 2)):
        min_heapify(A, i)


build_min_heap(massive)

fo.write(str(len(heap)))
fo.write("\n")
for h in heap:
    fo.write(str(h[0]))
    fo.write(" ")
    fo.write(str(h[1]))
    fo.write("\n")
