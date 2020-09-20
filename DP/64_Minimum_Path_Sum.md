# Problem Description
- Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

- Note: You can only move either down or right at any point in time.

- Example:

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```
## Solution
### Takeaway
- DP equation: dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
1. 注意理解这种dp问题的构造思路和写法
2. recursion with memoization / bottom-up iteration
3. 在这个问题中，由于只要保证先周边再中间的执行顺序，之前的grid值就不需要考虑，因此可以优化为space(1)
4. 事实证明从range(n) 改成while写法对space complexity影响不大...

```python
# space complexity O(n*m)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == None: return None
        m = len(grid)
        n = len(grid[0])
        i = j = 0
        # for i in range(m):
        while i < m:
            j = 0
            while j < n:
            # for j in range(n):
                if i == 0 and j == 0:
                    pass
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
                elif i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                j += 1
            i += 1
        return grid[-1][-1]
```

```python
# space complexity O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == None: return None
        m = len(grid)
        n = len(grid[0])
        i = j = 0
        # for i in range(m):
        while i < m:
            j = 0
            while j < n:
            # for j in range(n):
                if i == 0 and j == 0:
                    pass
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
                elif i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                j += 1
            i += 1
        return grid[-1][-1]
```
