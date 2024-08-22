# Inserting a key into a min heap
#   - place the new key at the first free leaf
#   - if parent > node swap up

def bubble_up(node):
    while node.parent and node.parent.key > node.key:
        copy = node.parent
        node.parent = node
        node = copy
# Height is O(log(N)) so bubble up is 0(log(N))

# Delete Minimum
#   -Head will be Minimum.
#   -Replace Head with smallest child
#   -Return min

def delete_min(node:Node) -> Node:
    while head is not a leaf:
        smallest_child = child of node with smallest key
        if smallest_child < node:
            swap node and smallest_child
            node = smallest_child
        else:
            break
# HEAP in Python
'''
https://github.com/python/cpython/blob/d3a8d616faf3364b22fde18dce8c168de9368146/Lib/heapq.py#L263
'''
import heapq

h = []
heapq.heappush(h, (5, "hello")
heapq.heappush(h, (6, "how are")
heapq.heappush(h, (8, "you")

heapq.heappop(h) # (5, "hello")
h[0] #(6, "how are")

# Heap works on an empty array on O(N) time complexity
h = [1,2,4,6,3,1,5]
heapq.heapify(h)
# Top 3 elements from HEAP
import heapq
def heap_top_3(arr: List[int]) -> List[int]:
    heapq.heapify(arr)
    res = []
    for i in range(3):
        res.append(heapq.heappop(arr))
    return res

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = heap_top_3(arr)
    print(' '.join(map(str, res)))


