class MinHeap:
    def __init__(self, array):
        self.post_travel_list = []
        self.pre_travel_list = []
        self.in_travel_list = []
        self.arr = array
        for elem in range(len(array) // 2, -1, -1):
            self.heapify(elem)

    def heapify(self, idx):
        while True:
            left_child = 2 * idx + 1
            right_child = (2 * idx) + 2
            largest_child = idx

            if left_child < len(self.arr) and self.arr[left_child] < self.arr[largest_child]:
                largest_child = left_child

            if right_child < len(self.arr) and self.arr[right_child] < self.arr[largest_child]:
                largest_child = right_child

            if largest_child == idx:
                break

            self.arr[idx], self.arr[largest_child] = self.arr[largest_child], self.arr[idx]
            idx = largest_child

    def __str__(self):
        return " ".join(list(map(str, self.arr)))

    def print(self):
        for root in range(0, len(self.arr) // 2):
            left = 2 * root + 1
            right = 2 * root + 2
            print(f"root: {self.arr[root]} ", end="")
            if left < len(self.arr):
                print(f"left: {self.arr[left]}")
            if right < len(self.arr):
                print(f"    right: {self.arr[right]}")

    def in_order_travel(self, idx_root):
        if idx_root >= len(self.arr):
            return
        self.in_order_travel((idx_root * 2) + 1)
        self.in_travel_list.append(self.arr[idx_root])
        self.in_order_travel((idx_root * 2) + 2)


    def pre_order_travel(self, idx_root):
        if idx_root >= len(self.arr):
            return
        self.pre_travel_list.append(self.arr[idx_root])
        self.pre_order_travel((idx_root * 2) + 1)
        self.pre_order_travel((idx_root * 2) + 2)


    def post_order_travel(self, idx_root):
        if idx_root >= len(self.arr):
            return
        self.post_order_travel(idx_root * 2 + 1)
        self.post_order_travel(idx_root * 2 + 2)
        self.post_travel_list.append(self.arr[idx_root])
