
# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Iterative solution
# We compare the values of the current nodes in both lists and append the smaller one to the merged list, then move the corresponding pointer forward. After one of the lists is exhausted, we append the remaining nodes of the other list.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()  # Create a dummy node to simplify edge cases
    tail = dummy       # Tail will point to the last node in the merged list
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1  # Append list1's node to the merged list
            list1 = list1.next  # Move to the next node in list1
        else:
            tail.next = list2  # Append list2's node to the merged list
            list2 = list2.next  # Move to the next node in list2
        tail = tail.next  # Move the tail pointer to the last node
    
    # If there are remaining nodes in either list, append them
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next  # The head of the merged list is the next node after dummy

# Time complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively. We traverse both lists once.
# Space complexity: O(1) since we are merging the lists in place and only using

# Recursive solution
# We compare the values of the current nodes in both lists and recursively merge the rest of the lists. The smaller node becomes the head of the merged list, and we set its next pointer to the result of merging the rest of the lists.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2  # If list1 is empty, return list2
    if not list2:
        return list1  # If list2 is empty, return list1
    
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)  # Merge the rest of list1 with list2
        return list1  # Return the head of the merged list
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)  # Merge list1 with the rest of list2
        return list2  # Return the head of the merged list
    
# Time complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively. We traverse both lists once.
# Space complexity: O(n + m) due to the recursive call stack. In the worst case, the depth of the recursion can be equal to the total number of nodes in both lists.