from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(pre_order: List[int], in_order: List[int]) -> TreeNode:
    """
    :param pre_order: 前序遍历
    :param in_order: 中序遍历
    :return: 根节点
    """
    if not pre_order or not in_order:
        return None
    root = TreeNode(pre_order[0])
    root_index = in_order.index(pre_order[0])
    root.left = build_tree(pre_order[1:root_index + 1], in_order[:root_index])
    root.right = build_tree(pre_order[root_index + 1:], in_order[root_index + 1:])
    return root


def solution(pre_order: List[int], in_order: List[int]) -> List[int]:
    """
    :param pre_order: 前序遍历
    :param in_order: 中序遍历
    :return: 层次遍历
    """
    # 先建树 再遍历
    root = build_tree(pre_order, in_order)
    ans = []
    queue = [root]
    while queue:
        cur = queue.pop(0)
        ans.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return ans


if __name__ == "__main__":
    pre_order = list(map(lambda x: int(x), input().split()))
    in_order = list(map(lambda x: int(x), input().split()))
    print(" ".join(map(lambda x: str(x), solution(pre_order, in_order))))