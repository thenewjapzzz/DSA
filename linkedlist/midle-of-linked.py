class Solution:
    def middleNode(self, head):
        ahead = head
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
        
        return head