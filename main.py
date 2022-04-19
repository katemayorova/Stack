from bracket_balance_checker import BracketBalanceChecker

if __name__ == '__main__':
    balanced_str = '[([])((([[[]]])))]{()}'
    print(BracketBalanceChecker.is_balanced(balanced_str))

