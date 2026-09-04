# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque([p])
        queueQ = deque([q])

        while queueP and queueQ:
            nodeP = queueP.popleft()
            nodeQ = queueQ.popleft()
    
            if not nodeP and not nodeQ:
                continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            queueP.append(nodeP.left)
            queueQ.append(nodeQ.left)
            queueP.append(nodeP.right)
            queueQ.append(nodeQ.right)
        return True
        