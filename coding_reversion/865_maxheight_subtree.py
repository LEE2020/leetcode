'''
给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。

如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。

一个节点的 子树 是该节点加上它的所有后代的集合。

返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点。

 

注意：本题与力扣 1123 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    

        if not root :
            return root
        else:
            left = self.maxheight(root.left)
            right = self.maxheight(root.right)
            if left <right:
                return self.subtreeWithAllDeepest(root.right)
            elif left > right:
                return self.subtreeWithAllDeepest(root.left)
            elif left == right:
                return root 
    

    def maxheight(self,root):
        if not root:
            return 0 
        else:
            return max(self.maxheight(root.left),self.maxheight(root.right))+1 

