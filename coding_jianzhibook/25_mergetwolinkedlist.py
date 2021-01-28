'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1 
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2 ) 
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        new_l3 = ListNode(None)
        dummy = new_l3 
        while l1 and l2:
            if l1.val <=l2.val:
                new_l3.next = l1 
                l1 = l1.next 
            else:
                new_l3.next = l2 
                l2 = l2.next 
            new_l3 = new_l3.next 

        new_l3.next = l1 if l1 else l2 
        return dummy.next 
