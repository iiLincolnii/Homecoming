def invert_list(head):
    if head.next is None:
        return head
 
    new_head = invert_list(head.next)
    #  1 - 2 - 3
    #  head是2 head.next是3 head.next.next是3的指向 2给3的指向，也就是3 - 2
    head.next.next = head
    # 2指向为空，防止成环
    head.next = None
    #  1指向2的 现在找1
    return new_head
 
 
# 顺序打印
def sort_list(ln):
    while ln:
        print(ln.val)
        ln = ln.next
 
 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
 
if __name__ == '__main__':
    l1 = ListNode(4)
    l1.next = ListNode(3)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)
    sort_list(l1)
    print(type(l1))
 
    l = invert_list(l1)
    sort_list(l)
