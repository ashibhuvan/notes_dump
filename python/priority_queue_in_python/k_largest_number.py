from typing import List
import heapq
def find_kth_largest(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    reverse = [-1 * num for num in nums]
    heapq.heapify(reverse)
    for i in range(k - 1):
        heapq.heappop(reverse)
    return reverse[0] * -1

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
