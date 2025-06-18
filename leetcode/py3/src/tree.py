from typing import Optional, List
from collections import deque

# Leetcode's definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Ha! definitily NOT what leetcode does for their tree representation.
# TODO: figure out later how they skip Nones for the tree to look like:
# [2,null,4,10,8,null,null,4]
def treeFromList(node_vals: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if node_vals is None or len(node_vals) == 0 or node_vals[0] is None:
        return None

    n = len(node_vals)

    def buildTree(root: TreeNode, i: int):
        li, ri = 2*i + 1, 2*i + 2
        if li < n and node_vals[li] is not None:
            lchild = TreeNode(node_vals[li])
            root.left = lchild
            buildTree(root.left, li)
        if ri < n and node_vals[ri] is not None:
            rchild = TreeNode(node_vals[ri])
            root.right = rchild
            buildTree(root.right, ri)

    root = TreeNode(node_vals[0])
    buildTree(root, 0)
    return root

def goodNodes(root: TreeNode) -> int:
    """ leetcode #1448 """

    if root is None:
        return 0

    def countGoodNodes(root: TreeNode, cur_max: int) -> int:
        if root is None:
            return 0

        res = 0
        if root.val >= cur_max:
            res += 1
            cur_max = root.val

        return res + countGoodNodes(root.left, cur_max) + countGoodNodes(root.right, cur_max)

    return 1 + countGoodNodes(root.left, root.val) + countGoodNodes(root.right, root.val)


