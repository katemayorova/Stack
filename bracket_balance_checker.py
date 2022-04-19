import re

from stack import Stack


class BracketBalanceChecker:
    __BRACKET_MAP = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    @staticmethod
    def is_balanced(string: str) -> bool:
        if not re.match('^[\\[\\](){}]*$', string):
            raise ValueError()
        stack = Stack()
        for i in string:
            if i in {'[', '(', '{'}:
                stack.push(i)
            elif stack.is_empty() or BracketBalanceChecker.__BRACKET_MAP[i] != stack.pop():
                return False
        return stack.is_empty()
