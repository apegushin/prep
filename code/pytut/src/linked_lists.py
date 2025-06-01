from typing import Optional
from typing import List
import heapq

class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next

class LinkedListLeetcode:
    def printLinkedList(self, l: Optional[ListNode], label: str = None):
        node = l
        print(f'{label}: ' if label is not None else '', end='')
        print('head -> ', end='')
        while node is not None:
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
        """ leetcode #2 """

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
        """ leetcode #203 """

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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ leetcode #206 """

        if head is None or head.next is None:
            return head

        rev = None
        while head:
            nxt = head.next
            head.next = rev
            rev = head
            head = nxt
        return rev

    def reverseNnodes(self, head: Optional[ListNode], num: int) -> Optional[ListNode]:
        if num < 2: return head

        last = head
        rev = None
        i = 0
        while head is not None and i < num:
            nxt = head.next
            head.next = rev
            rev = head
            head = nxt
            i += 1
        last.next = head
        return rev


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ leetcode #92 """

        if head is None or head.next is None or right - left == 0:
            return head

        prev = ListNode(0, head)
        h = prev
        i = 1
        while i < left and head is not None:
            i += 1
            prev, head = head, head.next

        rh = self.reverseNnodes(head, right - left + 1)
        prev.next = rh
        return h.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ leetcode #23 """

        class ComparableListNode:
            def __init__(self, l: ListNode):
                self.l = l
            def __lt__(self, o: ListNode):
                return self.l.val < o.l.val

        heads = []
        for list in lists:
            if list is not None:
                heapq.heappush(heads, ComparableListNode(list))

        head, curr = None, None
        while heads:
            min_head = heapq.heappop(heads)
            if min_head.l.next is not None:
                heapq.heappush(heads, ComparableListNode(min_head.l.next))

            if head is None:
                head = min_head.l
                curr = head
            else:
                curr.next = min_head.l
                curr = curr.next
            curr.next = None

        return head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        dummy = ListNode(0, head)
        prev = dummy
        cur1, cur2 = head, head.next

        while cur1 is not None and cur2 is not None:
            post = cur2.next
            prev.next = cur2
            cur2.next = cur1
            cur1.next = post
            prev = cur1
            cur1 = post
            cur2 = post.next if post is not None else None

        return dummy.next

if __name__ == '__main__':
    lllc = LinkedListLeetcode()

    h1 = lllc.createFromList([1,2,3,4,5])
    lllc.printLinkedList(h1, 'h1')

    h2 = lllc.createFromList([1,2,3,4,5,6,7,8])
    lllc.printLinkedList(h2, 'h2')

    h3 = lllc.createFromList([1,2,3,4,5,6,7,8,9,10,11])
    lllc.printLinkedList(h3, 'h3')

    h4 = lllc.mergeKLists([h1,h2,h3])
    lllc.printLinkedList(h4)

    # print(lllc.linkedList2List(h1))
    # h3 = lllc.reverseBetween(h1, 2, 4)
    # h3 = lllc.reverseNnodes(h2, 1)
    # lllc.printLinkedList(h3, 'h3')
    # print(lllc.linkedList2List(h2))

