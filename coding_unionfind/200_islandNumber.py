'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# 三种方法 bfs/dfs/union-find
class UnionFind(object):
    def __init__(self,n):
        self.father = {key:key for key in range(n)}
        
    def find(self,x):
        return self.father[x]
    def union(self,x,y):
        _x = self.find(x)
        _y = self.find(y)
        if _x != _y:
            for ind in self.father:
                if self.father[ind] ==_x:
                    self.father[ind] = _y 
        
            


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n_row = len(grid)
        n_col = len(grid[0])
            
        space = 0 
        
        def getind(x,y):
            return x*n_col + y  # 对应岛屿的表示，每个位置都是单独的岛屿 

        uf = UnionFind(n_row * n_col ) # 每个位置都是一个单独岛屿 
        for ind_x in range(n_row):
            for ind_y in range(n_col):
                if grid[ind_x][ind_y] == '0':
                    space += 1  # 非岛屿的部分也会记录在self.father中 
                if grid[ind_x][ind_y] == "1":
                    for i,j in [[1,0],[0,1],[-1,0],[0,-1]]: # 
                        tmpx = ind_x + i 
                        tmpy = ind_y + j 
                        if 0<= tmpx < n_row and 0<=tmpy < n_col and grid[tmpx][tmpy] == "1":
                            uf.union(getind(ind_x,ind_y),getind(tmpx,tmpy))
        
        return len(set(uf.father.values())) - space
        

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        visited 一定要配置 ， 
        nextlevel不一定，deque 不一定 
        """
        from collections import deque
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        global visited 
        visited = set() 
        def bfs(i, j):
            global visited
            queue = deque()
            queue.appendleft((i, j))
            visited.add((i,j))
            while queue:
                i, j = queue.pop()
                if (i,j) not in visited:
                    visited.add((i,j))
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1" and (tmp_i,tmp_j) not in visited:
                        visited.add((tmp_i,tmp_j))
                        queue.appendleft((tmp_i, tmp_j))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    cnt += 1
                    visited.add((i,j))
        return cnt


 


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

       dfs search for island numbers 

        """
        n_row = len(grid)
        n_col = len(grid[0])
        clusters = 0
        global visited 
        visited = set() 
        def dfs(i,j):
            if (i,j) not in visited:
                visited.add((i,j))
            for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0<= tmp_i < n_row and 0<=tmp_j<n_col and grid[tmp_i][tmp_j] =='1' and (tmp_i,tmp_j) not in visited:
                    dfs(tmp_i,tmp_j)

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    visited.add((i,j))
                    clusters += 1
        return clusters



        
        
