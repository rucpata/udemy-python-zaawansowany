f = lambda x: len(x)

print(f('a 19-letters strings'))

text_list = ['x','xxx','xxxxx','xxxxxxx','']

print(list(map(f, text_list)))

print(list(map(lambda s: len(s), text_list)))