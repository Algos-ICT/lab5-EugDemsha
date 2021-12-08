with open("Input", "r") as fi:
    lines = fi.read().split("\n")
fo = open("Output", "w")
n = int(lines[0])
array = [int(i) for i in lines[1].split()]
print(array)

def check_heap(array, n):
    for i in range(n):
        if 2 * i + 1 < n:
            if array[2 * i + 1] < array[i] or array[2 * i + 2] < array[i]:
                return "No"
    return "Yes"

fo.write(str(check_heap(array, n)))