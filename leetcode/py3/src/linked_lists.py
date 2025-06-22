from typing import Optional, List, Any
import heapq

class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next


def printLinkedList(l: Optional[ListNode], label: str = ''):
    node = l
    print(f'{label}: ' if label is not None else '', end='')
    print('head -> ', end='')
    while node is not None:
        print(f'{node.val} -> ', end='')
        node = node.next
    print('None')

def createFromList(nums: List[int]) -> Optional[ListNode]:
    head = None
    for e in reversed(nums):
        node = ListNode(e, head)
        head = node
    return head

def linkedList2List(l: Optional[ListNode]) -> List[int]:
    lst = []
    node = l
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
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

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
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

def reverseNnodes(head: Optional[ListNode], num: int) -> Optional[ListNode]:
    if head == None or num < 2: return head

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


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """ leetcode #92 """

    if head is None or head.next is None or right - left == 0:
        return head

    prev = ListNode(0, head)
    h = prev
    i = 1
    while i < left and head is not None:
        i += 1
        prev, head = head, head.next

    rh = reverseNnodes(head, right - left + 1)
    prev.next = rh
    return h.next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """ leetcode #23 """

    class ComparableListNode:
        def __init__(self, l: ListNode):
            self.l = l
        def __lt__(self, o: Any):
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
            curr.next = min_head.l # type: ignore
            curr = curr.next # type: ignore
        curr.next = None

    return head

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """ leetcode #24 """

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

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """ leetcode #148 """

    def mergeTwoSortedLists(h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur = dummy
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next

        if h1 is not None:
            cur.next = h1
        elif h2 is not None:
            cur.next = h2

        return dummy.next

    def mergeSortLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        fast, slow, temp = head, head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            temp = slow
            slow = slow.next # type: ignore

        temp.next = None # type: ignore
        left = mergeSortLinkedList(head)
        right = mergeSortLinkedList(slow)

        return mergeTwoSortedLists(left, right)

    return mergeSortLinkedList(head)

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """ leetcode #82 """

    if not head or not head.next: return head

    dummy = ListNode()
    cur = dummy

    while head:
        if head.next and head.val != head.next.val:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = None
        elif head.next and head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next
        else:
            cur.next = head
            head = head.next
    return dummy.next
