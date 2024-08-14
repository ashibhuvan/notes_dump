'''
tree : connected, acyclic, undirected graph

difference between a tree and graph is the possibility of having a cycle
handle this by using a variable 'visited' to keep track of verticies we have visited



When you are doing BFS on a graph, you use a queue because you want to add the children
of a node to behind the other nodes that were already added, so you only search at 1 level at a time

use a visited variable so you never queue up a neighbour that was already visited


'''
# BFS graph template in python


# Use a queue to track nodes to be visited
# Use a function that needs to be implemented to return the node's neighbors


from collections import deque

def bfs(root):
    queue = deque([root]]
    visited = set([root])

    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in getNeighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
    print("You reached the end of your code")

## Finding Distance and Tracking Level in BFS

def bfs(self, root):
    queue = deque([root])
    visited = set([root])
    level = 0

    while queue:
        n = len(queue) # This is how we know how many nodes are in the level because we will keep adding
        for _ in range(n):
            node = queue.popleft()
            for neighbor in getNeighbors(node):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
            level += 1
    print("You reached the end of your code")







        
