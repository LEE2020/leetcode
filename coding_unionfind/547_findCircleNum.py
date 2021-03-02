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
            

class UnionFind:
    def __init__(self,n):
        self.father = {key: key for key in range(n)}
        # 额外记录集合的数量
        # self.num_of_sets = 0
    
    def find(self,x):
        return self.father[x]
        """
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
        """
    
    def union(self,x,y):
        _x = self.find(x)
        _y = self.find(y)
        # 路径压缩
        if _x != _y:
            for ind in self.father:
                if self.father[ind] == _x :
                    self.father[ind] = _y 

        """
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1
        """
    """
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1

    """

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    uf.union(i,j)
        
        return len(set(uf.father.values())) 

    def findCircleNum(self, isConnected):
        """ bfs search for finding connected provinces
            当bfs需要用到层级时，才必须用nextlevel 区别开来；
            否则 直接append到queue中就好。
            而且，用简单的stack就好了。后入后出。



            一般建议用 collections.deque 
            queue = collections.deque()
            queue.appendleft()
            queue.pop() 
        """
        clusters = 0
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
