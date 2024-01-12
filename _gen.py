
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

def gen_fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a


