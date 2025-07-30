"""Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3"""

#DFS RE
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

#Time Complexity: O(n) where n is the number of nodes in the tree
#Space Complexity: O(h) where h is the height of the tree due to recursion stack

#DFS Iterative
def maxDepthIterative(root):
    if not root:
        return 0
    stack = [(root, 1)]  # (node, depth)
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return max_depth

#BFS Iterative
from collections import deque
def maxDepthBFS(root):
    if not root:
        return 0
    level=0
    q=deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
