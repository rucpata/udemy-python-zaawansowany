#exec() nie zwraca żadnej wartości

var_x = 10

source = '''
new_var = 1
for i in range(var_x):
    print('-' * i)
    new_var += 1
'''

result = exec(source)
print(result)

print(var_x)
print(new_var)

source = input('Enter your expressions: ')
print(eval(source))