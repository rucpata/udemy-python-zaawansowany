""" Ukrywanie pewnych właściwości które występują w klasie w taki sposób
aby nie można było ich zobaczyć ani zmodyfikować z zewnątrz.
PYTHONowe klasy nie bronią klas przed modyfikacją."""

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

#Instancje klasy /instance/
car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

car_02._Car__isOnSale = False #UDAŁO się ZMODYFIKOWAĆ KLASĘ
car_02.YearOfProduction = 2005 #DODANIE nowego atrybuty do danego obiektu
del car_02.YearOfProduction #usunięcie danego atrybutu dla klasy

setattr(car_02, 'TAXI', False) #metoda do dodawania nowej właściwości dla obiektu
delattr(car_02, 'TAXI') #usunięcie atrybutu
print(hasattr(car_02, 'TAXI'))#sprawdza czy obiekt posiada atrybut o wskazanej nazwie


car_02.GetInfo()
print(vars(car_02))