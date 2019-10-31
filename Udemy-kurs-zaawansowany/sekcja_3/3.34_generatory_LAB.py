ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((start, stop) for start in ports for stop in ports)

counter = 0
for (start, stop) in routes:
    print('{} - {}'.format(start, stop))
    counter += 1

print(counter)

print('*' * 40)

routes = ((start, stop) for start in ports for stop in ports if start != stop)
counter = 0
for (start, stop) in routes:
    print('{} - {}'.format(start, stop))
print(counter)


print('=' * 30)
gen = ((start, stop) for start in ports for stop in ports if start < stop)
print(gen)
counter= 0
for (start, stop) in gen:
    print('{} - {}'.format(start, stop))
print(gen)


print('//' * 30)
gen = ((start, stop) for start in ports for stop in ports if start < stop)
while True:
    try:
        print(next(gen))
    except:
        print('all values have been generated')
        break




