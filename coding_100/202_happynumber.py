'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        if slow == fast : 会cycle ，判断cycle时会是 sum ==1 的情况吗？ 这类问题，要相出退出循环的情况。

        """
        def bitsum(n):
            sum_ = 0 
            while n:
                bit = n%10 
                sum_ += bit ** 2
                n /= 10 
            return sum_ 
        slow = n
        fast = bitsum(n)
        while slow != fast:
            slow = bitsum(slow)
            fast = bitsum(bitsum(fast))
        return slow == 1 



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def bitsum(n):
            sum_ = 0 
            while n:
                bit = n%10 
                sum_ += bit ** 2
                n /= 10 
            return sum_ 
        a = set()
        while True:
            tmp = bitsum(n)
            if tmp not in a:    
                a.add(tmp)
            else:
                return False 
            if tmp == 1:
                return True 
            else:
                n = tmp 
        



