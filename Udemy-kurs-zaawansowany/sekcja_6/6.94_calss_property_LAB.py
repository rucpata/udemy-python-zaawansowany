class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
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
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>>Text can be set only for cake ({})'.format(name))

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

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>Text can be only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on tje cake')




cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', True, '')
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '', False, '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', True, 'Good Luck!')

print('Today in our offert:')
for c in Cake.bakery_offer:
    c.showInfo()

cake_01.Text = 'Happy birthday!'
cake_02.Text = '18'

for c in Cake.bakery_offer:
    c.showInfo()