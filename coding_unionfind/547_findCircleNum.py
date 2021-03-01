'''
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3 

'''

# 方法 1 bfs / dfs 
# 方法3 不带路径压缩的 union-find 
# 方法4 带路径压缩的 union-find
class UnionFind(object):
    def __init__(self,tmp_list ):
        self.father = dict()
        for ind in tmp_list:
            self.father[ind] = None  # 初始化时，本身的ID为cluster ID    
    def find(self,x):
        root = x 
        while root != None:
            root = self.father[root]
        return root # 返回该节点的最根部的节点（一个集合的头头）        
        
    def find_pathCompress(self,x): 
        root = x
        while root != None:
            root = self.father[root]
        # 路径压缩, 这条路径上的点，都指向根结点
        father  = x 
        while x  != root: 
            tmp_father = self.father[x] 
            self.father[x] = root 
            x = tmp_father  
        return root     
    def merge(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:        
            self.father[x] = y_root 

            
    

 
class Solution(object):
    def findCircleNum(self,isConnected):
        tmp_list = [t for t in range(len(isConnected))] 
        uf = UnionFind(tmp_list)
        for i_pro in range(len(isConnected)):
            for j_pro in range(i_pro):
                if isConnected[i_pro][j_pro] == 1:
                    uf.merge(i_pro,j_pro)
        
        return len(set(uf.father.values())) # 作为头头的数量 

    def findCircleNum(self, isConnected):
        """ bfs search for finding connected provinces 
        """
        circles = 0
        visited = set()
        n = len(isConnected) # provinces numbers 
        queen = [] 
        for i_pro in range(n):
            if i_pro not in visited:
                queen.append(i_pro)
                while queen:
                    j_pro = queen.pop()
                    visited.add(j_pro)
                    for k  in range(n):
                        if isConnected[j_pro][k]  == 1 and k not in visited:
                            queen.append(k)
                circles += 1

        return circles 

    def findCircleNum(self,isConnected):
        """ dfs search for finding connected provinces"""


        circles = 0 
        visited = set()
        n = len(isConnected)

        for i_pro in range(n):
            if i_pro not in visited:
                visited.add(i_pro)
                dfs(i_pro)
                circles += 1

        def dfs(i_pro):
            for j_pro in range(n):
                if isConnected[i_pro][j_pro] == 1 and j_pro not in visited:
                    visited.add(j_pro)
                    dfs(j_pro)


        return circles      
