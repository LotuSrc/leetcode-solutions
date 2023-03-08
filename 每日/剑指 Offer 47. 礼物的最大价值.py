class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 因为只能往右或者往下
        # 一维数组就可以完成二维dp
        dp = [0 for _ in range(len(grid[0]))]
        dp[0] = grid[0][0]
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[j] = max(dp[j], dp[j - 1]) + grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j]
        return dp[-1]