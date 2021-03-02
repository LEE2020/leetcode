'''
在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。

返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

 

示例 1：

输入：A = [0,1,0], K = 1
输出：2
解释：先翻转 A[0]，然后翻转 A[2]。
示例 2：

输入：A = [1,1,0], K = 2
输出：-1
解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        无限切分，从左到右的游戏                
        """

        """ 解法1 超时 
        rst = []
        cnt = 0
        for ind in range(len(A)-K +1):
            if A[ind] ==1:  # 判断当前的数是不是1，如果是的话，不处理
                continue
            for ind2 in range(K): # 将接下来的K个元素逐次的进行翻转
                A[ind+ind2] ^= 1
            cnt +=1 
        return cnt if sum(A) == len(A) else -1
        """
        
        n = len(A)
        queue = collections.deque() # 队列，可以控制pop哪边，add哪边
        res = 0
        for i in range(n):
            if queue and i >= queue[0] + K: # 如果当前的index 大于K的长度，则从左边弹出
                queue.popleft()
            if len(queue) % 2 == A[i]: # 如果当前A[i]已经经历了偶数次反转后仍然为偶数，则该数需要再反转；同理，经历了奇数次反转仍然是奇数，该数也是需要再反转
                if i + K > n: # 如果超出了长度，说明剩下的数已经不足K个，return -1 
                    return -1
                queue.append(i) # 否则记录一次反转次数
                res += 1        
        return res

