class Solution:
    def lastStoneWeight(self, stones:List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()

            if first != second:
                stones.append(first - second)
        return stones[0] if stones else 0
