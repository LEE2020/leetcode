'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pre = ListNode() # 万一第一个节点就要反转，可以增加这个节点。
        pre.next = head 
        cnt = 0 
        node = pre  
        
        while left - cnt != 1 :
            pre = pre.next 
            cnt += 1 
        
        pre_tmp = pre  
        x = self.reverseList(pre_tmp ,right,cnt) # 需要记住前置节点，因为还要串起来 
        pre.next  = x 
        return  node.next  


    def reverseList(self,pre,right,cnt):
        pre = pre 
        cur = pre.next
        tmp2 = cur  
        while cur:
            tmp = cur.next
            cur.next = pre 
            pre = cur 
            cur = tmp 
            cnt += 1
            if cnt == right:
                break 
        tmp2.next = cur 
        return pre


