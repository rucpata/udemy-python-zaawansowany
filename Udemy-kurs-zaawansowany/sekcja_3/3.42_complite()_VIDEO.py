import time
source = 'reportLine += 1' #zwiększa numer liniki generowanego raportu

reportLine = 0

start = time.time()
for i in range(100000):
    exec(source)

stop = time.time()
time_not_compiled = stop - start

start = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
time_comiled = stop - start

print(time_not_compiled)
print(time_comiled)
print(time_not_compiled/time_comiled)
# kompitalcja (compilate)