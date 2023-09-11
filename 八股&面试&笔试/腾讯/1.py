from collections import Counter


# 路径
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回节点权值1个数比0的个数多一的路径数
# @param root TreeNode类 权值为0和1的二叉树根节点
# @return int整型
#
class Solution:
    def pathNumber(self, root: TreeNode) -> int:
        # write code here
        self.val_list = []
        self.dfs(root, [])
        counter = Counter(self.val_list)  # val -> cnt
        ans = 0

        # 路径值->路径数
        for val, cnt in counter.items():
            ans += counter[val - 1] * cnt  #
        return ans

    def dfs(self, root, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            self.val_list.append(sum(path))
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.right = TreeNode(1)
    print(Solution().pathNumber(root))
