# small value

n = 10
sq5 = (5 ** (1/2))
F = ( pow((1 + sq5) / 2, n) - pow(((1 - sq5) / 2), n) ) / sq5

# last number of big value
n = 132941
def fibonacci(n, m=10):
    fib1 = 1
    fib2 = 1
    for i in range(2, n):
        fib = (fib1 + fib2) % m
        fib1, fib2 = fib2, fib
    return fib

# last / m

n = 10
m = 11

fibPrev = 0
fib = 1
cached = [fibPrev, fib]

for curr in range(1, n):

    fibOld = fib
    fib = (fib + fibPrev) % m
    fibPrev = fibOld

    if fibPrev == 0 and fib == 1:
        cached.pop()
        break
    else:
        cached.append(fib)

offset = n % len(cached)
print(cached[offset])