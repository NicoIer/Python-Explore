import sys

if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    m = len(grid)
    n = len(grid[0])
    ans = 0


    def dfs(i, j, cur):

        cur = cur + grid[i][j]  # 当前值
        if i == m - 1 and j == n - 1:  # 到达左下角
            return cur
        if i == m - 1:
            return dfs(i, j + 1, cur)
        if j == n - 1:
            return dfs(i + 1, j, cur)
        # 往右 往左
        return max(dfs(i + 1, j, cur), dfs(i, j + 1, cur))


    print(dfs(0, 0, 0))
