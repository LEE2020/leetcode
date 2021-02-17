'''
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

 


mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-diagonal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rst = 0 

        def helper(mat):
            if len(mat) == 1:
                return mat[0][0]
            if mat ==[]:
                return 0 
            #tmp_mat = mat[1:-1][0][1:-1]
            tmp = []
            tmp_mat = [] 
            for ind_i in range(1,len(mat)-1):
                for ind_j in range(1,len(mat[0])-1):
                    tmp.append(mat[ind_i][ind_j])
                    
                tmp_mat.append(tmp)
                tmp = [] 
            # 矩阵的四个角 + 递归（new_mat）的值，即可。 

            tmp_sum = mat[0][0] + mat[0][-1]+mat[-1][0] + mat[-1][-1]
            
            return helper(tmp_mat) + tmp_sum 
        rst = helper(mat)
        return rst 

