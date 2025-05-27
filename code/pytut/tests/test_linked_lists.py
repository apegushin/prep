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

