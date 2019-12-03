#cache = przechowuje wyniki wczesniejszych utuchomien danej funkcji
import time
import functools

@functools.lru_cache()
def Factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Factorial(i)))

stop = time.time()
print('Execution time', stop-start)

print(Factorial.cache_info()) # ile wyników zostało cache i ile razy udało się  tego skrozystać