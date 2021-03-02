'''
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 

示例：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 
        i = len(nums)-1
        j = len(nums)-1
        if nums==[]:
            self.dp = [] 
        else:
            '''
            self.dp = [[0 for ind in range(j+1) ]  for ind in range(i+1)]
            self.dp[0][0] = self.nums[0]

            for ind_x in range(i+1):
                for ind_y  in range(ind_x,j+1):
                    self.dp[ind_x][ind_y] = self.dp[ind_x][ind_y-1]+ self.nums[ind_y]
            '''
            self.dp = [0]*(len(nums))
            self.dp[0] = nums[0]

            for ind in range(1,len(nums)):
                self.dp[ind] = self.dp[ind-1]+self.nums[ind]
               

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0 and j==0:
            return self.nums[0]
        if len(self.nums) == 0 :
            return [] 
        else:  
            ''' return self.dp[i][j]'''
            return self.dp[j] - self.dp[i] + self.nums[i]
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
