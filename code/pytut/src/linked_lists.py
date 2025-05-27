from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next

class LinkedListLeetcode:
    def printLinkedList(self, l: Optional[ListNode]):
        node = l
        print('head -> ', end='')
        while node != None:
            print(f'{node.val} -> ', end='')
            node = node.next
        print('None')

    def createFromList(self, nums: List[int]) -> Optional[ListNode]:
        head = None
        for e in reversed(nums):
            node = ListNode(e, head)
            head = node
        return head

    def linkedList2List(self, l: Optional[ListNode]) -> List[int]:
        lst = []
        node = l
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        head = ListNode(0, None)
        curr = head
        carry_over = 0
        while l1 is not None or l2 is not None or carry_over:
            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0
            total = l1val + l2val + carry_over
            carry_over = total // 10
            total %= 10
            curr.val = total
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is not None or l2 is not None or carry_over:
                curr.next = ListNode(0, None)
                curr = curr.next
        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if head is None:
            return head

        h = head
        while h.next:
            if h.next.val != val:
                h = h.next
            else:
                h.next = h.next.next
        return head

if __name__ == '__main__':
    lllc = LinkedListLeetcode()

    h1 = lllc.createFromList([2,4,3])
    print(lllc.linkedList2List(h1))

