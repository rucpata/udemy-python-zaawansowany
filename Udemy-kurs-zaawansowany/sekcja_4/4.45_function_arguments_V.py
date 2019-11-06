def BuyMe(prefix = 'Please buy me',
          what='something nice'): # wartość domyślna dla jednego argumentu
    print(prefix, what)

#Przekazywanie argumentu przez pozycje
BuyMe('Please buy me', 'a new car')

# Przekazywanie wartości argumentu przez nazwę
BuyMe(prefix='Please buy me', what='a car')
BuyMe(what='a brand new car', prefix= 'Please buy me')
BuyMe('Please')
BuyMe(prefix='Please buy me')
BuyMe(what='something sweet')

# przesyłanie argumentów w sposób JAWNY