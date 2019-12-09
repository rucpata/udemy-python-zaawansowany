"""Dekoratory klasy"""
brandOneSale = 'Opel'


class Car:

    numberOfCars = 0
    listOfCars = []

    #metoda instancji
    def __init__(self, brand, model, isAirBagOk, carIsPaintingOk, carIsMechanicOk, isOnSale):#jakie właściwości ma klasa
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.carIsPaintingOk = carIsPaintingOk
        self.carIsMechanicOk = carIsMechanicOk
        self.__isOnSale = isOnSale #__ oznacza że jest wewnętrzne, systemowe

    # udostępnia ukryty atrybut
    def __GetIsOnSale(self):
        return self.__isOnSale

    @property  # odwoływanie do IsOnSale tak jakby to była funkcja przestaje działać, wadą jest to że teraz nie da się zminić wartości
    def IsOnSale(self):
        return self.__isOnSale

    # zmiana wartości atrybuty
    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOneSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chanching status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOneSale))

    #WŁAŚCIWOŚCI = (1.przy pomocy jakiej metody klasy jesteśmy w stanie pobierać wartość tej zmiennej, 2.jaka metoda ma
    # by używana do zmieniania tej wartości, 3.funkcja która może usunąć ten atrybut, 4. opcjonalny-może definiować
    # dokumentacje dla tej właściwości

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()

car_01 = Car('Seat', 'Ibiza', True, True, True, False)

print(car_01.IsOnSale)
car_01.IsOnSale = True
del car_01.IsOnSale
print(car_01.IsOnSale)
print(car_01.CarTitle)
