from typing import List
import heapq

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    heap = []
    for row in matrix:
        heapq.heappush(heap, (row[0], row, 0))
    for i in range(k - 1):
        val, row, idx = heapq.heappop(heap)
        if idx < len(row) - 1: #Not at the last Element Yet
            heapq.heappush(heap, (row[idx + 1], row, idx + 1))
    return heap[0][0]   


if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = kth_smallest(matrix, k)
    print(res)
