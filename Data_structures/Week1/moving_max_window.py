# queue with 2 stacks,
# get min O(1)

test = """8\n2 7 3 1 5 2 6 2\n4"""

data = test.split('\n')
n = int(data[0])
m = int(data[2])
data = data[1].strip().split()

# add first m-1 elements to push stack
stack_push = []
stack_pop = []
for i, v in enumerate(data[:m-1]):
    v = int(v)
    if stack_push:
        stack_push.append([v, max(v, stack_push[-1][1])])
    else:
        stack_push.append([v, v])

for e in data[m-1:]:
    push = int(e)
    # push
    if stack_push:
        stack_push.append([push, max(push, stack_push[-1][1])])
    else:
        stack_push.append([push, push])
    # move and pop
    if not stack_pop:
        while stack_push:
            move = stack_push.pop()[0]
            if not stack_pop:
                stack_pop.append([move, move])
            else:
                stack_pop.append([move, max(move, stack_pop[-1][1])])
    max_pop = stack_pop.pop()[1]
    # max
    if stack_push:
        max_ = max(max_pop, stack_push[-1][1])
    else:
        max_ = max_pop
    print(max_, end=" ")
