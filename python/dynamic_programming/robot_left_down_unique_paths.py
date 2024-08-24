def unique_paths(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for idx,row in enumerate(dp):
        for jdx,cell in enumerate(row):
            if jdx == 0 and idx == 0:
                continue
            
            left = 0
            above = 0
            
            # Check Left
            if jdx > 0:
                left += dp[idx][jdx - 1]
            # Check Above
            if idx > 0:
                above += dp[idx - 1][jdx]
            dp[idx][jdx] = left + above
   
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)
