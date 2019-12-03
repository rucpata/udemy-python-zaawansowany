import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for i in range(50):
    result = fib(i)
    print('{} {}'.format(i, result))
stop = time.time()

print('Execution time', stop - start)
print(fib.cache_info())