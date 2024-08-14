# DFS in python for graph
# Use Recursive Call Stack to Keep Traveling


def dfs(node, visited)
    if not node: return

    for neighbor in getNeighbors(node):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
    print ("You have reached the end of your code", node, visited)


# Now do it for trees!

def dfs(root, target):
    if root is None:
        return None

    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left:
        return left
    return dfs(root.right, target)
    
