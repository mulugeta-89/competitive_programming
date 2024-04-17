# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, head = [], ListNode()
        for i, item in enumerate(lists):
            if item:
                heappush(heap, (item.val, i, item))
        temp = head
        while heap:
            _, i, item = heappop(heap)

            if item.next:
                heappush(heap, (item.next.val, i, item.next))
            temp.next = item
            temp = temp.next
        return head.next


        