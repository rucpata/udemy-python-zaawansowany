"""Jak zaimplementować funkcję, czy samochód jest uszkodzony.
Funkcja stanie się elementem składowym klasy."""

class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, carIsPaintingOk, carIsMechanicOk): #jakie właściwości ma klasa
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.carIsPaintingOk = carIsPaintingOk
        self.carIsMechanicOk = carIsMechanicOk
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOk and self.carIsPaintingOk and self.carIsMechanicOk)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag   - ok -            {}'.format(self.isAirBagOk))
        print('Painting  - ok -            {}'.format(self.carIsPaintingOk))
        print('Mechanic  - ok -            {}'.format(self.carIsMechanicOk))
        print('----------------------------------')

print('Class level variable BEFORE creating instances:', Car.numberOfCars, Car.listOfCars)

#Instancje klasy /instance/
car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print('Class level vawiables AFTER creating instance:', Car.numberOfCars, Car.listOfCars)

# sprawdzenie id dla klasy i instancji
print('Id of class is:', id(Car))
print('Id of instance are:', id(car_01), id(car_02))

#Jeśli chcemy sprawdzić czy dana instancja należy do danej klasy
print('Check if object belongs to class', isinstance(car_01, Car))
print('Check if oject belongs to class using type:', type(car_01) is Car)
print('Check class of an object using_class:', car_01.__class__)

#Pozwala nam sprawdzić obiekt od środka: informacje o poszczególnych atrybutach obiektu.
print('List of instance attributes with values:', vars(car_01)) # informacje o atrybutach danej klasy
print('list od class attributes with value:    ', vars(Car)) #informacje o tej klasie ale nie o instancjach klasy

#odkrywa wewnętrznie inne metody, które sa przed nami schowana
print('List of instance attributes with values:', dir(car_01))
print('List od class attributes with values:   ', dir(Car))

print('Valute taken from instance:', car_01.numberOfCars, 'Value taken from class', Car.numberOfCars)