'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
动态规划，找最大值的路径
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) ==1 and len(grid[0])==1:
            return grid[0][0]
        m = len(grid)
        n = len(grid[0])
        df =[[0 for ind in range(n)] for ind in range(m)]
        #df[0][0] = 0

        for ind_x in range(m):
            for ind_y in range(n):
                df[ind_x][ind_y] = max(df[ind_x-1][ind_y],df[ind_x][ind_y-1])+grid[ind_x][ind_y]
        return df[-1][-1]

