# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        
        
        
        smallest = 10**5
        index_of_smallest = -1
        flag = False
        for i in range(len(lists)):
            if lists[i] is not None:
                flag = True
                if lists[i].val < smallest:
                    smallest = lists[i].val
                    index_of_smallest = i
        if flag:
            lists[index_of_smallest] = lists[index_of_smallest].next 
        else:
            return None
        
        head = ListNode(smallest)
        tail = head
        
        flag = True
        while flag:
            
            smallest = 10**5
            flag = False
            index_of_smallest = -1
            for i in range(len(lists)):
                if lists[i] is not None:
                    flag = True
                    if lists[i].val < smallest:
                        smallest = lists[i].val
                        index_of_smallest = i
            if flag:
                lists[index_of_smallest] = lists[index_of_smallest].next
                tail.next = ListNode(smallest)
                tail = tail.next
                        
        return head
