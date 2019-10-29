dayType = 4

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
   pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = 'weekedn' if dayType == 1 else 'workday' if dayType == 2 else 'holiday'
print(dayDescription)

print ('weekedn') if dayType == 1 else print('workday') if dayType == 2 else print('holiday')