import pytest
from src import strings

class TestStringLeetcodeProblems:

    def setup_method(self, method):
        print(f'setting up test for {method}')

    def teardown_method(self, method):
        print(f'tearing down after test for {method}')

    def testOne(self):
        assert True