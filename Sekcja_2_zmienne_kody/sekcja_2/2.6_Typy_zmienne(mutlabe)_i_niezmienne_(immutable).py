number = 10
print('Variable number:', number, id(number))
number += 2
print('Variable number:', number, id(number))

text = 'Africa'
print('Variable text:', text, id(text))
text +=' is hot'
print('Variable text:', text, id(text))

list = [1, 2, 3]
print('Variable list:', list, id(list))
list.append(4)
print('Variable list:', list, id(list))

list2 = list
print('Variable list2:', list2, id(list2))
list2.append(5)
print('Variable list:', list, id(list))
print('Variable list2:', list2, id(list2))
# Element 5 został dodany zarówno do zmienej list jak i list2.
# List i list2 wskazują na ten sam obszar pamięci.

list3 = list.copy()
print('Variable list:', list, id(list))
print('Variable list3:', list3, id(list3))
list3.append(6)
print('Variable list:', list, id(list))
print('Variable list3:', list3, id(list3))