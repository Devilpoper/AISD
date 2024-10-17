from heapq import heapify


class MinHeap:
    def __init__(self, arr):
        self.arr = arr
        for i in range(len(arr) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, idx):
        while True:
            left_child = 2 * idx + 1
            right_child = (2 * idx) + 2
            largest_child = idx

            if left_child < len(self.arr) and self.arr[left_child] > self.arr[largest_child]:
                largest_child = left_child

            if right_child < len(self.arr) and self.arr[right_child] > self.arr[largest_child]:
                largest_child = right_child

            if largest_child == idx:
                break

            self.arr[idx], self.arr[largest_child] = self.arr[largest_child], self.arr[idx]
            idx = largest_child

    def __str__(self):
        return " ".join(list(map(str, self.arr)))

    def print(self):
        for i in range(0, len(arr)//2):
            left = 2 * i + 1
            right = 2 * i + 2
            print(f"root: {arr[i]} ", end="")
            if left < len(arr):
                print(f"left: {arr[left]}")
            if right < len(arr):
                print(f"    right: {arr[right]}")


arr = [1, 2, 3, 4, 5, 6, 7, 8]
heap = MinHeap(arr)
print(heap)
heap.print()