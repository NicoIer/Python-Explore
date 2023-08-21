def dfs(cur: int, i: int, j: int) -> bool:
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return True
    if i >= len(grid) or j >= len(grid[0]) or visited[i][j]:
        return False
    cur += grid[i][j]
    visited[i][j] = True
    if cur < 0:
        return False

    if dfs(cur, i + 1, j) or dfs(cur, i, j + 1):
        return True
    visited[i][j] = False
    return False


if __name__ == '__main__':
    grid = [[1, 2, 3, 4],
            [4, 5, 1, 3],
            [4, 5, 1, 3],
            [4, 5, 1, 3]]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # 
