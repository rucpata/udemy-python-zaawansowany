import os

path = r'/Users/wlasciciel/Desktop/programowanie/udemy/python/Python dla średnio zaawansowanych/mydata.txt'

#instrukcja usuwająca plik
#os.remove(path)

"""
if os.path.isfile(path): #bada czy plik istnieje
    print('File %s exists ' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created ' % path)
"""

result = os.path.isfile(path) or open(path,'x').close() #isfile - czy plik istnieje?
print(result)