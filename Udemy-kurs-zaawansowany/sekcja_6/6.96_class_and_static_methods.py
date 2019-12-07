"""Właściwości kalsy."""
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

    # metoda klasy
    @classmethod
    def ReadFromText(cls, aText): #cls - skrót od klas
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    # metoda statyczna - niezależna od całej klasy // są umieszczone w klasie to jedynie dla porządku
    @staticmethod
    def Convert_KM_KW(KM):
        return KM *0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW*1.36

#czyta dane z pliku tekstowego
lineOfText = 'Renault:Megan:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)
car_03.GetInfo()

print('converting 120 KM to KW', Car.Convert_KM_KW(120))
print('converting 90 KW to KM', Car.Convert_KW_KM(90))

print(car_03.ReadFromText(lineOfText))
print(car_03.Convert_KW_KM(50))

