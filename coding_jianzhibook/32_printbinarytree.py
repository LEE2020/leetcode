'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]

bfs 打印二叉树 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queen = [root]
        next_level = []
        visited = [root.val]
        
        while queen:
            
            next_level = [] 
            for node in queen:

                neighs = [] 
                if node.left:
                    neighs.append(node.left)
                if node.right:
                    neighs.append(node.right)
                for ind in neighs:
                    
                    #if ind.val not in visited:
                    visited.append(ind.val)
                    next_level.append(ind)
            queen = next_level 
        return visited
