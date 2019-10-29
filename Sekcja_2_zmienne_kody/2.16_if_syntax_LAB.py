"""
Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)
"""
price = 123
bonus = 23
bonus_granted = True
price = price - bonus if bonus_granted else price
print(price)

print('\n')
"""
Zapisz poniższe polecenie if w postaci uproszczonej:

rating = 5
 
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
"""

rating = 1
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

print('\n')
"""
Napisz program, który:

zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia

bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić

Przepisz powyższy program stosując składnie uproszczona polecenia if
"""

import datetime as dt
today_weekday = dt.date.today().strftime('%A')

if today_weekday == "Monday":
    print("Pomagam mamie")
elif today_weekday == "Tuesday":
    print('Pranie.')
elif today_weekday == "Wednesday":
    print('Pranie')
elif today_weekday == "Thursday ":
    print('Dyżur.')
elif today_weekday == "Friday":
    print('Zebrania')
elif today_weekday == "Saturday":
    print('Lekcje')
else:
    print('Będzie dla nas')

print('Pomogam mamie' if today_weekday == 'Monday')