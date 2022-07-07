if __name__ == '__main__':
    x = [1, 2]
    y = [[2, 1], [2, 3], [3, 4]]
    print(x in y)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = 0
        
        tail = head.next
        tail.prev = head
        while tail.next:
            tail.next.prev = tail
            tail = tail.next
            
        left = head
        right = tail
        
        while left != right:
            val = left.val + right.val
            if val > max_val:
                max_val = val
            left = left.next
            if left == right:
                break
            right = right.prev
        
        return max_val
            


    class Solution:
        def pairSum(self, head: Optional[ListNode]) -> int:
            max_val = 0
            arr = []

            slow = head
            fast = head
            while fast and fast.next:
                arr.append(slow.val)
                slow = slow.next
                fast = fast.next.next

            for i in range(len(arr)-1, -1, -1):
                max_val = max(arr[i] + slow.val, max_val)
                slow = slow.next

            return max_val