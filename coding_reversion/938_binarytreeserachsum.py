'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

 

示例 1：


输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
示例 2：


输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        global res 
        res = 0 
        def helper(root,low,high):
            global res 
            if  root is None:
                return 0
            if root.left  is None and  root.right is None  :
                return root.val if root.val <=high and root.val >=low else 0  

            left_ = helper(root.left,low,high)
            right_ = helper(root.right,low,high)
            tmp = root.val if root.val <= high and root.val >=low else 0 
            return tmp+left_ +right_ 
        
        return helper(root,low,high )
