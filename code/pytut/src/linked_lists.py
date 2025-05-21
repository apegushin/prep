from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next

class LinkedListLeetcodeProblems:
    def __init__(self):
        pass

    def print_list(self, head: Optional[ListNode]):
        while head != None:
            print(f'{head.val} -> ', end="")
            head = head.next
        print('None')

    def create_list(self, size: int = 10) -> Optional[ListNode]:
        if size == 0:
            return None
        head = ListNode(0)
        curr = head
        for i in range(1, size):
            curr.next = ListNode(i)
            curr = curr.next
        return head

    def create_list_from_seq(self, l: list = []) -> Optional[ListNode]:
        if len(l) == 0:
            return None
        head = ListNode(l[0])
        curr = head
        for e in l[1:]:
            curr.next = ListNode(e)
            curr = curr.next
        return head


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


if __name__ == '__main__':
    lllp = LinkedListLeetcodeProblems()
    head1 = lllp.create_list_from_seq([2,4,3])
    head2 = lllp.create_list_from_seq([5,6,4])
    head3 = lllp.addTwoNumbers(head1, head2)
    lllp.print_list(head3)
