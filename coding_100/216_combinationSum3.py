'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 浅拷贝 path[:] ， reference to path's copy()
path 

'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
     
        if k <=0 or k > n or n <=0 :
            return []
        path = []
        def helper(k,residue,start,path): 
            global res 
            if residue < 0:
                return 
            if k == 0:
                if residue ==0:
                    
                    res.append(path[:]) # 需要进行浅拷贝，这时的path已经清空 
                    #print(path,path[:])
                    return 
                return 
            for ind in range(start,10):
                path.append(ind) 
                helper(k-1,residue - ind,ind+ 1 , path)
                #print(k,residue,path,res)
                path.pop()  # 影响path值 
        global res
        res = [] 
        helper(k,n,1,path)
        return res
        
        """
        方法二
        res = []
        def helper(path,start,n,k):
            if n==0 and k==0:
                res.append(path[:])
                return 
            for ind in range(start,10):
                path.append(ind)
                helper(path,ind+1,n-ind,k-1)
                path.pop()
        helper([],1,n,k)

        return res 
        """


