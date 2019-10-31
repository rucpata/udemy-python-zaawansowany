# funkcja EVAL = pozwala pobrac od użytkownika jakiś napis który będzie fragmentem kodu

var_x = 10
password = "My super secret password"

source = '__import__("os").getcwd()'

# globals = globals().copy()
# del globals['password']

globals = {}
result = eval(source, globals)
print(result)

#print(globals())

