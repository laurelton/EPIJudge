from test_framework import generic_test


def evaluate(expression: str) -> int:
    values = []
    fn = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x,
    }

    delimiter = ','
    operands = expression.split(delimiter)
    
    for s in operands:
        if s.isdigit():
            num = int(s)
            values.append(num)
        else:
            op1 = values.pop()
            op2 = values.pop()
            result = fn[s](op1, op2)
            values.append(result)

    return values[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
