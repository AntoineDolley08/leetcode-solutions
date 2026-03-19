
# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Iterative solution

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev to the current node
        current = next_node       # Move to the next node
    
    return prev  # At the end, prev will be the new head of the reversed list

# Time complexity: O(n) where n is the number of nodes in the linked list. We visit each node once.
# Space complexity: O(1) since we are using only a constant amount of extra space

# Recursive solution

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head  # Base case: if the list is empty or has only one node, it's already reversed
    
    new_head = self.reverseList(head.next)  # Reverse the rest of the list
    head.next.next = head  # Make the next node point to the current node
    head.next = None       # Set the current node's next to None
    
    return new_head  # Return the new head of the reversed list

# Time complexity: O(n) where n is the number of nodes in the linked list. We visit each node once.
# Space complexity: O(n) due to the recursive call stack. In the worst case, the depth of the recursion can be equal to the number of nodes in the linked list.