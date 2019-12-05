class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
        self.name = name
        if kind in self.know_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free

    def showInfo(self):
        print('{}'.format(self.name).upper())
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t{}'.format(a))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('Gluten: free: {}'.format(self.__gluten_free))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)



cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', True)
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '', False)
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', True)

print('Today in our offert:')
for c in Cake.bakery_offer:
    c.showInfo()

cake_03.__gluten_free = False
print(dir(cake_03))
cake_03._Cake__gluten_free = False
cake_03.show_info()