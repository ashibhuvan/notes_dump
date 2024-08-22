from typing import list
import heapq
import math

def k_closest_points(points: List[List[int]], k: int) -> List[int]:
    res = []
    heap = []

    for i in range(len(points)):
        coords = points[i]
        distance = math.sqrt(coords[0] ** 2 + coords[1] ** 2)

        heapq.heappush(heap, (distance, i))
    
    for j in range(k):
        res.append(points[heapq.heappop(heap)[1]])
    return res
