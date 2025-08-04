#Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r=[]
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: r.append(level)
        return r
    
    #BFS #NO LEVEL STACK EMPTY