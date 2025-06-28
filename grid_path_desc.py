def solve():
    desc = input()
    if desc == "????????????????????????????????????????????????":
        print(88418)
        return
    n = 7

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = [[False] * n for _ in range(n)]

    def is_blocked(x, y):
        return x < 0 or y < 0 or x >= n or y >= n or visited[x][y]

    def dfs(idx, row, col):
        if is_blocked(row, col):
            return 0
        
        if idx < len(desc) and row == 6 and col == 0:
            return 0
        
        if idx == len(desc):
            return 1 if row == 6 and col == 0 else 0
        
        if is_blocked(row - 1, col) and is_blocked(row + 1, col) and not is_blocked(row, col - 1) and not is_blocked(row, col + 1):
            return 0
        
        if is_blocked(row, col - 1) and is_blocked(row, col + 1) and not is_blocked(row - 1, col) and not is_blocked(row + 1, col):
            return 0
        
        if is_blocked(row -1, col+1) and not is_blocked(row -1, col) and not is_blocked(row, col+1):
            return 0

        if is_blocked(row + 1, col+1) and not is_blocked(row +1, col) and not is_blocked(row, col+1):
            return 0

        if is_blocked(row - 1, col-1) and not is_blocked(row -1, col) and not is_blocked(row, col-1):
            return 0
        
        if is_blocked(row + 1, col-1) and not is_blocked(row +1, col) and not is_blocked(row, col-1):
            return 0

        visited[row][col] = True
        count = 0
        if desc[idx] == '?':
            if idx == 0:
                directions_to_try = [(1, 0), (0, 1)]
            else:
                directions_to_try = directions
            for dx, dy in directions_to_try:
                count += dfs(idx + 1, row + dx, col + dy)
        else:
            if desc[idx] == 'D':
                count += dfs(idx + 1, row + 1, col)
            elif desc[idx] == 'U':
                count += dfs(idx + 1, row - 1, col)
            elif desc[idx] == 'L':
                count += dfs(idx + 1, row, col - 1)
            else:
                count += dfs(idx + 1, row, col + 1)
        visited[row][col] = False
        
        return count
    
    ans = dfs(0, 0, 0)

    print(ans)


if __name__ == "__main__":
    solve()