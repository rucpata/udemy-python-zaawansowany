"""Właściwości kalsy."""
brandOneSale = 'Opel'


class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, carIsPaintingOk, carIsMechanicOk, isOnSale): #jakie właściwości ma klasa
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.carIsPaintingOk = carIsPaintingOk
        self.carIsMechanicOk = carIsMechanicOk
        self.__isOnSale = isOnSale #__ oznacza że jest wewnętrzne, systemowe
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.carIsPaintingOk and self.carIsMechanicOk)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -            {}'.format(self.isAirBagOk))
        print('Painting  - ok -            {}'.format(self.carIsPaintingOk))
        print('Mechanic  - ok -            {}'.format(self.carIsMechanicOk))
        print('IS ON SALE                  {}'.format(self.__isOnSale))
        print('----------------------------------')

    # udostępnia ukryty atrybut
    def __GetIsOnSale(self):
        return self.__isOnSale

    # zmiana wartości atrybuty
    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOneSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chanching status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOneSale))

    #WŁAŚCIWOŚCI = (1.przy pomocy jakiej metody klasy jesteśmy w stanie pobierać wartość tej zmiennej, 2.jaka metoda ma
    # by używana do zmieniania tej wartości, 3.funkcja która może usunąć ten atrybut, 4. opcjonalny-może definiować
    # dokumentacje dla tej właściwości
    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')

#Instancje klasy /instance/
car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

#nie używać takiej metody
print('Status of cars:', car_01._Car__GetIsOnSale(), car_02._Car__GetIsOnSale())
'''car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())
'''

car_01.IsOnSale = True
car_02.IsOnSale = True
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)