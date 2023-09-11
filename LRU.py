import io
import sys


class Node:
    def __init__(self, val: int):
        self.next: Node = None
        self.prev: Node = None
        self.val: int = val


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head: Node = None  # 双向循环链表
        self.tail: Node = None

    def put(self, key, value):
        if key not in self.dic and len(self.dic) == self.capacity:
            print("put", key, "最少使用的", self.tail.val)
            self.dic.pop(self.tail.val)  # 移除最近最少使用的
            self.tail = self.tail.prev
            self.remove(key)
            self.add(key)
            return
        if len(self.dic) > self.capacity:  # 超出容量
            self.dic.pop(self.tail.val)  # 移除最近最少使用的
            self.tail = self.tail.prev
            self.remove(key)
            self.add(key)
            return
        # 更新
        self.dic[key] = value
        self.remove(key)
        self.add(key)

    def remove(self, key):
        if not self.head:
            return
        cur = self.head
        while cur.next != self.head:
            if cur.val == key:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next

    def add(self, key):
        node = Node(key)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
            return
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.tail.next = node
        self.head = node

    def get(self, key):
        # print(key, self.dic)
        if key in self.dic:
            self.remove(key)
            self.add(key)
            return self.dic[key]
        else:
            return -1


def solution(radius: int):
    x_min = -radius
    x_max = radius
    y_min = -radius
    y_max = radius
    ans = [[" "] * (2 * radius + 1) for _ in range(2 * radius + 1)]
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if x * x + y * y <= radius * radius:
                ans[x + radius][y + radius] = "*"
    for i in range(len(ans)):
        print(ans[i])


# 0000
# 0000
# 0000
# 0000
if __name__ == "__main__":
    solution(4)
