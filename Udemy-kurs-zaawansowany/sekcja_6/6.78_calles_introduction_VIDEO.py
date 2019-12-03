car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibiza',
'carIsAirBagOk' : True,
'carIsPaintingOk' : True,
'carIsMechanicOk' : True
}

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOk' : True,
'carIsPaintingOk' : False,
'carIsMechanicOk' : True
}

def IsCarDamaged(aCar):
    return not(aCar['carIsAirBagOk'] and aCar['carIsPaintingOk'] and aCar['carIsMechanicOk'])

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print('{} {} damaged = {}'.format(c['carBrand'], c['carModel'], IsCarDamaged(c)))