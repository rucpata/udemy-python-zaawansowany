class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

print('Today in our offert:')
for c in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {}, illed with {}'.format(c.name, c.kind, c.taste,
                                                                                c.additives, c.filling))