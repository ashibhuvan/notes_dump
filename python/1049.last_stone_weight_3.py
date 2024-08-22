'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
'''
'''
Found this problem to be quite challenging if not familiar with Knapsack problem.
First step is to realize you want to greate 2 groups that can sum to the sum of all the stones.
2 subsets, both have a sum of SUM / 2. 
Then you want to find the maximum sum you can generate of any subset that is <= SUM // 2. This maximizing of subset sum
MINIMIZES the difference of the 2 subsets, thus finding the minimal weight left over after all stones are divided
'''

def solve(stones: List[int]) -> int:
    if not stones:
        return 0

    target = sum(stones) // 2
    dp = [0] * (target + 1)
    
    for stone in stones:
        for j in range(target, stone - 1, -1):
            dp[j] = max(dp[j], dp[j-stone] + stone)
    return sum(stones) - 2 * dp[j]
