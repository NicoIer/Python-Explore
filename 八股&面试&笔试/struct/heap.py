import functools
from typing import List


class MinHeap:
    """
    最小堆
    """

    def __init__(self, array: List[int] = None):
        self.array: List[int] = array if array else []
        self.__heapify()

    def pop(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop()
        first = self.array[0]
        self.array[0] = self.array.pop()
        self.__sink(0)
        return first

    def push(self, value: int):
        self.array.append(value)
        self.__swim(len(self.array) - 1)

    def __heapify(self):
        for i in range(len(self.array) - 1, -1, -1):
            self.__sink(i)

    def __sink(self, index):
        # 下沉 找到两个子节点 中最小的那个 与自己交换位置 如果自己是最小的 那么就不用下沉了 否则 交换位置 继续下沉
        left = index * 2 + 1
        right = index * 2 + 2

        # 找到最小的子节点
        min_index = index
        if left < len(self.array) and self.array[left] < self.array[min_index]:
            min_index = left
        if right < len(self.array) and self.array[right] < self.array[min_index]:
            min_index = right

        # 如果最小的子节点不是自己，那么就下沉
        if min_index != index:
            self.array[min_index], self.array[index] = self.array[index], self.array[min_index]
            self.__sink(min_index)

    def __len__(self) -> int:
        return len(self.array)

    @staticmethod
    def __get_parent_index(index: int) -> int:
        return (index - 1) >> 1

    def __swim(self, index):
        parent_index = self.__get_parent_index(index)
        while parent_index >= 0 and self.array[parent_index] > self.array[index]:
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            index = parent_index
            parent_index = self.__get_parent_index(index)


if __name__ == "__main__":
    heap = MinHeap()
    nums = [4, 6, 1, 3, -4]
    for num in nums:
        heap.push(num)
    while len(heap) > 0:
        print(heap.pop())

    import heapq
    nums = [4, 6, 1, 3, -4]
    heapq.heapify(nums)
    while len(nums) > 0:
        print(heapq.heappop(nums))

