# Fibonacci with Top Down with Memoization

def fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return n
    res = fib(n-1) + fib(n-2)
    memo[n] = res
    return res
# Fib with Bottom Up
def fib(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        res = dp[i - 1] + dp[i + 1]
        dp[i] = res
    return dp[-1]

