class MaxHeap:
    def __init__(self, arr):
        self.arr = arr

        for i in range(len(self.arr), -1, -1):
            self.heapify(i)

    def heapify(self, index):
        while True:
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            biggest_child = index

            if left_child < len(self.arr) and self.arr[left_child] > self.arr[biggest_child]:
                biggest_child = left_child
            if right_child < len(self.arr) and self.arr[right_child] > self.arr[biggest_child]:
                biggest_child = right_child

            if biggest_child == index:
                break

            self.arr[index], self.arr[biggest_child] = self.arr[biggest_child], self.arr[index]
            index = biggest_child

    def add(self, val):
        self.arr.append(val)
        pos = len(self.arr) - 1
        parent = (pos - 1) // 2
        while pos > 0 and self.arr[parent] < self.arr[pos]:
            self.arr[parent], self.arr[pos] = self.arr[pos], self.arr[parent]
            pos = parent
            parent = (pos - 1)//2


    def print(self):
        for root in range(0, len(self.arr) // 2):
            left = 2 * root + 1
            right = 2 * root + 2
            print(f"root: {self.arr[root]} ", end="")
            if left < len(self.arr):
                print(f"left: {self.arr[left]}")
            if right < len(self.arr):
                print(f"    right: {self.arr[right]}")

heap = MaxHeap([])
for i in [1, 2, 3, 4, 5, 6]:
    heap.add(i)

heap.print()