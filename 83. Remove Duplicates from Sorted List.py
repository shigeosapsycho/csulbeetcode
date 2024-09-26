class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head # initialize the pointer
        if not head:
            return None
        # Traverse the list while there are at least two nodes to compare (current and current.next)
        while current and current.next: 
            if current.val == current.next.val:
                # Skip the next node by making current.next point to current.next.next
                # This removes the duplicate from the list
                current.next = current.next.next
                pass
            else:
                current = current.next # If the current node is unique (no duplicate), move to the next node
        return head # After processing the entire list, return the modified head of the list
        
# 33 ms O(n), LinkedList problem solved on my own!