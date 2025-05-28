from src.linked_lists import LinkedListLeetcode

class TestLinkedListLeetcode:

    def setup_method(self, method):
        self.lllc = LinkedListLeetcode()

    def test_addTwoNumbers(self):
        h1 = self.lllc.createFromList([2,4,3])
        h2 = self.lllc.createFromList([5,6,4])
        h3 = self.lllc.addTwoNumbers(h1, h2)
        l3 = self.lllc.linkedList2List(h3)
        l3.reverse()
        assert l3 == [8, 0, 7]

    def test_removeElements(self):
        h1 = self.lllc.createFromList([1,2,6,3,4,5,6])
        h2 = self.lllc.removeElements(h1, 6)
        assert self.lllc.linkedList2List(h2) == [1,2,3,4,5]

    def test_reverseBetween(self):
        h1 = self.lllc.createFromList([1,2,3,4,5])
        h2 = self.lllc.reverseBetween(h1, 2, 4)
        assert self.lllc.linkedList2List(h2) == [1,4,3,2,5]

    def test_reverse(self):
        l1 = [1,2,3,4,5]
        h1 = self.lllc.createFromList(l1)
        h2 = self.lllc.reverseList(h1)
        l1.reverse()
        l2 = self.lllc.linkedList2List(h2)
        assert l1 == l2

