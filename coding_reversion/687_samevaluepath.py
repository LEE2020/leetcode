'''
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-univalue-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        global length 
        length  = 0 
        self.maxlength(root,root.val)
        return length
    def maxlength(self,root,val):
        global length 
        if not root:
            return 0
        left = self.maxlength(root.left,root.val)
        right = self.maxlength(root.right,root.val)
        length = max(length,left+right)
        if root.val == val :
            return max(left,right)+1
        return 0 
