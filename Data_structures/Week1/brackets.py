# list = stack
# collections.deque = two-sided stack

def check_brackets(input_str):

    from collections import deque

    stack = deque()
    stack_index = deque()

    brackets = {"}": "{",
                "]": "[",
                ")": "("}
    close_brackets = brackets.keys()
    open_brackets = brackets.values()

    for i, s in enumerate(input_str, 1):
        if s in close_brackets:
            if stack:
                if brackets[s] == stack.pop():
                    stack_index.pop()
                else:
                    return i
            else:
                return i
        if s in open_brackets:
            stack.append(s)
            stack_index.append(i)
    if stack:
        return stack_index.popleft()
    else:
        return "Success"

test_dict = {
    "()[": 3,
    "()": "Success",
    "{}[]": "Success",
    "[()]": "Success",
    "(())": "Success",
    "{[]}()": "Success",
    "{{": 1,
    "{[}": 3,
    "foo(bar);": "Success",
    "foo(bar[i);": 10
}

for s in test_dict.keys():
    assert check_brackets(s) == test_dict[s], s
