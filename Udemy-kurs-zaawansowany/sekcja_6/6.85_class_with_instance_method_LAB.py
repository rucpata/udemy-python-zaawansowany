class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

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

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

cake_01.showInfo()

cake_02.set_filling('vanilla cream')
cake_03.add_additives(['cocoa powder', 'coconuts'])

print('Today in our offert:')
for c in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {}, illed with {}'.format(c.name, c.kind, c.taste,
                                                                                c.additives, c.filling))
