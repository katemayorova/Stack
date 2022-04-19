from unittest import TestCase

from stack import Stack


class TestStack(TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push('123')
        self.assertFalse(self.stack.is_empty())

    def test_push_pop(self):
        self.stack.push('123')
        self.stack.push('456')
        self.assertEqual(self.stack.pop(), '456')
        self.assertEqual(self.stack.pop(), '123')

    def test_pop_empty(self):
        self.assertRaisesRegex(IndexError, 'В стеке больше нет элементов', self.stack.pop)

    def test_peek(self):
        self.stack.push('123')
        self.stack.push('456')
        peek = self.stack.peek()
        self.assertEqual(peek, self.stack.peek())
        self.assertEqual(peek, '456')

    def test_peek_empty(self):
        self.assertRaisesRegex(IndexError, 'В стеке больше нет элементов', self.stack.peek)

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push('123')
        self.stack.push('456')
        self.assertEqual(self.stack.size(), 2)

    def test_push_all(self):
        test_value = [1, 2, 3, 'lfegke', 'egkhhj', {'key': 'value'}]
        self.stack.push_all(test_value)
        for e in reversed(test_value):
            self.assertEqual(e, self.stack.pop())
