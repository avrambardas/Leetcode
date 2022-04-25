# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        ll1 = []
        ll2 = []
        while l1 is not None:
            ll1.append(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            ll2.append(l2.val)
            l2 = l2.next
            
        ll1 = ll1[::-1]
        ll2 = ll2[::-1]

        num1 = 0
        mul = 10**(len(ll1)-1)
        for num in ll1:
            num1 += num*mul
            mul = mul/10

        num2 = 0
        mul = 10**(len(ll2)-1)
        for num in ll2:
            num2 += num*mul
            mul = mul/10

        sum1 = list(str(int(num1 + num2)))[::-1]
        sum1 = [int(x) for x in sum1]
        
        head = ListNode(sum1[0])
        tail = head
        e=1
        while e < len(sum1):
            tail.next = ListNode(sum1[e])
            tail = tail.next
            e+=1
        return head
