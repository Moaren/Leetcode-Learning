# Problem Description
- Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

- You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Solution
- Takeaway
1. 注意topological转换中各个变量代表的实际意义，比如本题的dp中i和j不止代表采取的操作，也表示操作对象str的转换
2. 本题中insert, delete, replace都能保证让原string 向着target“更进一步”，难点是探究后续的长远影响

### Topological / Bottom-up solution
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2: return 0
        if word1 == None or word2 == None: return len(word1 or word2)
        m = len(word1)
        n = len(word2)
        # Assume m > n
        # In this problem, the cost of delete and insert are the same. So the order doesn't matter.
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for j in range(m + 1):
            dp[j][0] = j
        for i in range(n + 1):
            dp[0][i] = i
        for j in range(1,m+1):
             for i in range(1,n+1):
                    if word1[j-1] == word2[i-1]:
                        dp[j][i] = dp[j-1][i-1]
                    else:
                        dp[j][i] = min(dp[j-1][i],dp[j][i-1],dp[j-1][i-1]) + 1
        return dp[-1][-1]
```