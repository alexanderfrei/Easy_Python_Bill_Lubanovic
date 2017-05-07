# stack with max() support
# list of commands: pop, push, max

import sys

test = """5\npush 2\npush 1\nmax\npop\nmax"""
test = """10\npush 2\npush 3\npush 9\npush 7\npush 2\nmax\nmax\nmax\npop\nmax"""
test = """5\npush 1\npush 2\nmax\npop\nmax"""

stack_val = []
stack_max = []
for command in test.split('\n')[1:-1]:
    command = command.strip()
    print(command)
    if command == "pop":
        stack_max.pop()
        stack_val.pop()
    elif command == "max":
        print(stack_max[-1])
    else:
        push = int(command.split()[1])
        stack_val.append(push)
        if not stack_max:
            stack_max.append(push)
        else:
            stack_max.append(max(push, stack_max[-1]))
