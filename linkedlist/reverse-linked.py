def reverseList(head):
    new_list = None

    while head:
        next_node = head.next
        head.next = new_list
        new_list = head
        head = next_node
    
    return new_list