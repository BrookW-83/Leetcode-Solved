# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        heapq.heapify(minHeap)
        
        for i in range(len(lists)):
            if lists[i]:
                temp = lists[i].val
                lists[i] = lists[i].next
                heapq.heappush(minHeap,[temp,i])
                
        head = ListNode()
        node = head
        
        while minHeap:
            val, index = heapq.heappop(minHeap)
            curr = ListNode(val = val)
            node.next = curr
            node = node.next
            
            if lists[index]:
                temp = lists[index].val
                lists[index] = lists[index].next
                heapq.heappush(minHeap,[temp,index])
                
        return head.next
            