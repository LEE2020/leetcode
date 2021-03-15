'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        global rst 
        rst = []
        def helper(matrix):
            global rst 
            m = len(matrix)
            n = len(matrix[0])
            r1 = matrix[0]
            r2 = [ tmp[-1] for tmp in matrix[1:]] # matrix 的第一行到所有行
            r3 = [matrix[-1][i] for i in range(n -2 ,-1, -1  )] if m > 1 else [] # matrix 最后一行 ， 去除最后一列中的那一行，已经在r2中打印了。
            r4 = [line[0] for line in [matrix[i] for i in range(m - 2, 0, -1)]] if n > 1 else []
            rst += r1+r2+r3+r4 
            submatrix = [tmp[1:-1] for tmp in matrix[1:-1]]
            if len(submatrix) >0  and len(submatrix[0])>0 :
                helper(submatrix)
            
        helper(matrix)
        return rst 

