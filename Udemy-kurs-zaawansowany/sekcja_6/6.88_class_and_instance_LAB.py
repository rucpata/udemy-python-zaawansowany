class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.know_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def showInfo(self):
        print('{}'.format(self.name).upper())
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t{}'.format(a))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)



cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

print('Today in our offert:')
for c in Cake.bakery_offer:
    c.showInfo()

print('Is cake_01 of type Cake? (isinstance)', isinstance(cake_01, Cake))
print('Is cake_01 of type Cake? (type)', type(cake_01) is Cake)
print('vars cake_01', vars(cake_01))
print('vars Cake', vars(Cake))
print('dir cake_01', dir(cake_01))
print('dir Cake', dir(Cake))
