'''
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

 

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \    
    1   3  

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global rst
        rst = []
        def helper(root):
            global rst
            if root:
                rst.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        tmp = float('inf')
        
        for ind_x in range(len(rst)):
            for ind_y in range(ind_x+1,len(rst)):
                if ind_x == ind_y:
                    continue
                tmp = min(tmp,abs(rst[ind_x]-rst[ind_y]))

        return tmp



