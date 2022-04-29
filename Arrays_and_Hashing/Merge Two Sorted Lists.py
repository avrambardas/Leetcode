# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            head = ListNode(list2.val)
            tail = head
            list2 = list2.next
        else:
            head = ListNode(list1.val)
            tail = head
            list1 = list1.next
        
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
            else:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
        
        if list1 is None:
            while list2 is not None:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
        else:
            while list1 is not None:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
        return head
