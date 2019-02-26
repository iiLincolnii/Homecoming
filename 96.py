# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :type: ListNode
        """
        #单元素链表，返回空
        if not head.next:
            return

        #算出链表元素个数
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1

        #cur获得待删除元素，pre获取到删除元素的上一个元素
        pre, cur = head, head
        if count == n:
            pre.val = pre.next.val
            pre.next = pre.next.next
        for _ in range(count - n):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head
