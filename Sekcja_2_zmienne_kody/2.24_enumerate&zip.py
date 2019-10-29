workDays = [12, 21, 22, 21, 20, 22]

print(workDays)

print(workDays[2])

enumeratDays = list(enumerate(workDays))
print(enumeratDays)

for pos, value in enumeratDays:
    print('Position ', pos, 'value', value)

# zip = ma za zadanie połączyć dwie niezależne listy
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = list(zip(months, workDays))
print(monthsDays)

for m, d in monthsDays:
    print('Month', m, 'days', d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days', d)