from src.linked_lists import LinkedListLeetcode

class TestLinkedListLeetcode:

    def setup_method(self, method):
        self.lllp = LinkedListLeetcode()

    def test_addTwoNumbers(self):
        head1 = self.lllp.create_list_from_seq([2,4,3])
        head2 = self.lllp.create_list_from_seq([5,6,4])
        head3 = self.lllp.addTwoNumbers(head1, head2)
        assert True

