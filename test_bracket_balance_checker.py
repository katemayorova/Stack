from unittest import TestCase
from bracket_balance_checker import BracketBalanceChecker


class TestBracketBalanceChecker(TestCase):
    def test_is_balanced_positive(self):
        self.assertTrue(BracketBalanceChecker.is_balanced('(((([{}]))))'))
        self.assertTrue(BracketBalanceChecker.is_balanced('[([])((([[[]]])))]{()}'))
        self.assertTrue(BracketBalanceChecker.is_balanced('{{[()]}}'))

    def test_is_balanced_negative(self):
        self.assertFalse(BracketBalanceChecker.is_balanced('}{}'))
        self.assertFalse(BracketBalanceChecker.is_balanced('{{[(])]}}'))
        self.assertFalse(BracketBalanceChecker.is_balanced('[[{())}]'))

    def test_is_balanced_empty(self):
        self.assertTrue(BracketBalanceChecker.is_balanced(""))

    def test_is_balanced_garbage(self):
        self.assertRaises(Exception, BracketBalanceChecker.is_balanced, 'fasdifwoie')
