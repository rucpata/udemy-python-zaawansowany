"""Jak zaimplementować funkcję, czy samochód jest uszkodzony.
Funkcja stanie się elementem składowym klasy."""

class Car:

    def __init__(self, brand, model, isAirBagOk, carIsPaintingOk, carIsMechanicOk): #jakie właściwości ma klasa
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.carIsPaintingOk = carIsPaintingOk
        self.carIsMechanicOk = carIsMechanicOk

    def IsDamaged(self):
        return not (self.isAirBagOk and self.carIsPaintingOk and self.carIsMechanicOk)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -            {}'.format(self.isAirBagOk))
        print('Painting  - ok -            {}'.format(self.carIsPaintingOk))
        print('Mechanic  - ok -            {}'.format(self.carIsMechanicOk))
        print('----------------------------------')

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

car_01.GetInfo()
car_02.GetInfo()

print(car_01.brand, car_01.model, car_01.IsDamaged())
print(car_02.brand, car_02.model, car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.carIsPaintingOk, car_01.carIsMechanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.carIsPaintingOk, car_02.carIsMechanicOk)

'''

def IsCarDamaged(aCar):
    return not(aCar['carIsAirBagOk'] and aCar['carIsPaintingOk'] and aCar['carIsMechanicOk'])

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01, car_02]

for c in cars:
    print('{} {} damaged = {}'.form
'''