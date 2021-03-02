'''
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。


上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

 

示例：

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            n_row = 0 
            n_col = 0 
        else:
            n_row = len(matrix)
            n_col = len(matrix[0])
        self.presum = [[0 for _ in range(n_col+1)] for _ in range(n_row+1)]
        for indx in range(n_row):
            for indy in range(n_col):
                self.presum[indx+1][indy+1] = self.presum[indx][indy+1] + self.presum[indx+1][indy] - self.presum[indx][indy] + matrix[indx][indy]
                # 考虑到matrix 的 row,col 范围【0，n_row-1 】 ，【0，n_col-1】 
         
        
         


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

